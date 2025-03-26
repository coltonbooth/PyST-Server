# SensorThings Hub

This project implements a SensorThings API-compliant service built with FastAPI and SQLAlchemy. It serves as a central hub to collect, store, and serve sensor observations, metadata, actuator tasks, and related data from multiple IoT sensor nodes.

---

## Features

- **RESTful API:** Conforms to OGC SensorThings specification (sensing and tasking).
- **Database Persistence:** Stores data persistently in a SQLite database.
- **Automatic Validation:** Uses FastAPI with Pydantic for request validation and response formatting.
- **CORS Enabled:** Easily integrates with frontend clients or external systems.

---

## Setup & Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd <repo-directory>
```

2. Install required dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

---

## Running the Server

Run the FastAPI application locally:

```bash
python main.py
```

The service will be available at:

```
http://localhost:8000/v1
```

---

## Example API Usage

### Creating resources

See the following examples to initially set up resources on your hub:

- **Create Thing**:

```http
POST /v1/Things
{
  "id": 1,
  "name": "LoRa Node 1",
  "description": "Field-deployed LoRa sensor node."
}
```

- **Create Sensor**:

```http
POST /v1/Sensors
{
  "id": 1,
  "name": "Temperature Sensor",
  "description": "Measures temperature",
  "encodingType": "application/pdf",
  "metadata_": "http://example.com/datasheet.pdf"
}
```

- **Create Observed Property**:

```http
POST /v1/ObservedProperties
{
  "id": 1,
  "name": "Air Temperature",
  "description": "Temperature of ambient air",
  "definition": "http://dbpedia.org/page/Air_temperature"
}
```

- **Create Datastream** (associates Thing, Sensor, Observed Property):

```http
POST /v1/Datastreams
{
  "id": 1,
  "name": "Node 1 Air Temperature Stream",
  "description": "Temperature data stream",
  "observationType": "OM_ComplexObservation",
  "unitOfMeasurement": {
    "name": "Degree Celsius",
    "symbol": "°C",
    "definition": "http://unitsofmeasure.org/ucum.html#para-30"
  },
  "thing_id": 1,
  "sensor_id": 1,
  "observed_property_id": 1
}
```

### Posting observations (sensor data)

Typical incoming request from a sensor node:

```http
POST /v1/Observations
{
  "id": 1,
  "phenomenonTime": "2025-03-26T11:15:00Z",
  "resultTime": "2025-03-26T11:15:05Z",
  "result": 23.7,
  "datastream_id": 1
}
```

---

## Retrieving Data

- **List Observations:**

```http
GET /v1/Observations
```

- **Get specific Observation:**

```http
GET /v1/Observations/{observation_id}
```

---

## Database

Data is stored in the SQLite database located at:

```
pyst.db
```

---

## Extending the Service

To extend the API, modify:

- `models.py` – Define new data models.
- `main.py` – Implement corresponding API endpoints.

---

## Contributing

Contributions and improvements are welcome. Please open a pull request.

---

## License

Apache 2.0

