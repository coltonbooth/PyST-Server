# SensorThings API Server Overview

This server is an implementation of the **SensorThings API** using [FastAPI](https://fastapi.tiangolo.com/). It provides endpoints to manage and interact with both sensing and tasking aspects of IoT systems. The API is divided into two main sections: **Sensing** and **Tasking**.

## Sensing Endpoints

The Sensing endpoints allow clients to create, retrieve, and list various sensor-related resources such as:
- **Things**: Represent physical objects or entities.
- **Locations**: Specify geographical positions or areas.
- **Sensors**: Capture sensor metadata and information.
- **Observed Properties**: Define the properties being observed (e.g., temperature, humidity).
- **Datastreams**: Link Things, Sensors, and Observed Properties together to create data streams.
- **Observations**: Store sensor measurements with timestamps.
- **Features of Interest**: Provide context to observed data by defining specific areas or regions.

## Tasking Endpoints

The Tasking endpoints enable control of devices and include:
- **Actuators**: Devices that perform actions.
- **Tasking Capabilities**: Define the actions an actuator can perform.
- **Tasks**: Commands to be executed by actuators.

## Implementation Details

The server uses in-memory dictionaries for storage and Pydantic models for data validation. It implements basic error handling with FastAPI's HTTPException to ensure robust API interactions. This lightweight server serves as a demonstration of the SensorThings API and can be extended for production use.
---
# cURL Commands for SensorThings API
---

## Sensing Endpoints
### 1.	Create a Thing:
```bash
curl -X POST “http://localhost:8000/Things”
```
-H “Content-Type: application/json”
-d “{"id": 1, "name": "Sample Thing", "description": "A sample thing"}”
### 2.	List Things:
```bash
curl -X GET “http://localhost:8000/Things”
```
### 3.	Get a Specific Thing (id=1):
```bash
curl -X GET “http://localhost:8000/Things/1”
```
### 4.	Create a Location:
```bash
curl -X POST “http://localhost:8000/Locations”
```
-H “Content-Type: application/json”
-d “{"id": 1, "name": "Sample Location", "description": "A sample location", "encodingType": "application/vnd.geo+json", "location": {"type": "Point", "coordinates": [125.6, 10.1]}}”
### 5.	List Locations:
```bash
curl -X GET “http://localhost:8000/Locations”
```
### 6.	Get a Specific Location (id=1):
```bash
curl -X GET “http://localhost:8000/Locations/1”
```
### 7.	Create a Sensor:
```bash
curl -X POST “http://localhost:8000/Sensors”
```
-H “Content-Type: application/json”
-d “{"id": 1, "name": "Temperature Sensor", "description": "A sample sensor", "encodingType": "application/json", "metadata": "sensor metadata"}”
### 8.	List Sensors:
```bash
curl -X GET “http://localhost:8000/Sensors”
```
### 9.	Get a Specific Sensor (id=1):
```bash
curl -X GET “http://localhost:8000/Sensors/1”
```
### 10.	Create an ObservedProperty:
```bash
curl -X POST “http://localhost:8000/ObservedProperties”
```
-H “Content-Type: application/json”
-d “{"id": 1, "name": "Temperature", "description": "Temperature observed", "definition": "http://unitsofmeasure.org/ucum.html#para-30"}”
### 11.	List ObservedProperties:
```bash
curl -X GET “http://localhost:8000/ObservedProperties”
```
### 12.	Get a Specific ObservedProperty (id=1):
```bash
curl -X GET “http://localhost:8000/ObservedProperties/1”
```
### 13.	Create a Datastream:
```bash
curl -X POST “http://localhost:8000/Datastreams”
```
-H “Content-Type: application/json”
-d “{"id": 1, "name": "Temperature Datastream", "description": "Datastream for temperature", "observationType": "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement", "unitOfMeasurement": {"name": "degree Celsius", "symbol": "°C", "definition": "http://unitsofmeasure.org/ucum.html#para-30"}, "thing_id": 1, "sensor_id": 1, "observed_property_id": 1}”
### 14.	List Datastreams:
```bash
curl -X GET “http://localhost:8000/Datastreams”
```
### 15.	Get a Specific Datastream (id=1):
```bash
curl -X GET “http://localhost:8000/Datastreams/1”
```
### 16.	Create an Observation:
```bash
curl -X POST “http://localhost:8000/Observations”
```
-H “Content-Type: application/json”
-d “{"id": 1, "phenomenonTime": "2025-03-25T12:00:00Z", "resultTime": "2025-03-25T12:00:00Z", "result": 23.5, "datastream_id": 1}”
### 17.	List Observations:
```bash
curl -X GET “http://localhost:8000/Observations”
```
### 18.	Get a Specific Observation (id=1):
```bash
curl -X GET “http://localhost:8000/Observations/1”
```
### 19.	Create a FeatureOfInterest:
```bash
curl -X POST “http://localhost:8000/FeaturesOfInterest”
```
-H “Content-Type: application/json”
-d “{"id": 1, "name": "Area of Interest", "description": "A specific region", "encodingType": "application/vnd.geo+json", "feature": {"type": "Polygon", "coordinates": [[[30, 10], [40, 40], [20, 40], [10, 20], [30, 10]]]}}”
### 20.	List FeaturesOfInterest:
```bash
curl -X GET “http://localhost:8000/FeaturesOfInterest”
```
### 21.	Get a Specific FeatureOfInterest (id=1):
```bash
curl -X GET “http://localhost:8000/FeaturesOfInterest/1”
```

⸻

## Tasking Endpoints
### 22.	Create an Actuator:
```bash
curl -X POST “http://localhost:8000/Actuators”
```
-H “Content-Type: application/json”
-d “{"id": 1, "name": "Valve Actuator", "description": "Controls a valve", "encodingType": "application/json", "metadata": "actuator metadata"}”
### 23.	List Actuators:
```bash
curl -X GET “http://localhost:8000/Actuators”
```
### 24.	Get a Specific Actuator (id=1):
```bash
curl -X GET “http://localhost:8000/Actuators/1”
```
### 25.	Create a TaskingCapability:
```bash
curl -X POST “http://localhost:8000/TaskingCapabilities”
```
-H “Content-Type: application/json”
-d “{"id": 1, "name": "Valve Control", "description": "Capability to control valve", "actuator_id": 1}”
### 26.	List TaskingCapabilities:
```bash
curl -X GET “http://localhost:8000/TaskingCapabilities”
```
### 27.	Get a Specific TaskingCapability (id=1):
```bash
curl -X GET “http://localhost:8000/TaskingCapabilities/1”
```
### 28.	Create a Task:
```bash
curl -X POST “http://localhost:8000/Tasks”
```
-H “Content-Type: application/json”
-d “{"id": 1, "taskingCapability_id": 1, "command": "Open Valve", "parameters": {"duration": 10}, "status": "pending"}”
### 29.	List Tasks:
```bash
curl -X GET “http://localhost:8000/Tasks”
```
### 30.	Get a Specific Task (id=1):
```bash
curl -X GET “http://localhost:8000/Tasks/1”
```

---
# Postman Guide for SensorThings API Endpoints
---

Below is a summary guide you can use in Postman. For each endpoint, the URL, HTTP method, and sample JSON (if applicable) are provided.

## Sensing Endpoints
### 1.	Create a Thing
	•	URL: http://localhost:8000/Things
	•	Method: POST
	•	Body (JSON):

{
  "id": 1,
  "name": "Sample Thing",
  "description": "A sample thing"
}


### 2.	List Things
	•	URL: http://localhost:8000/Things
	•	Method: GET
### 3.	Get a Specific Thing
	•	URL: http://localhost:8000/Things/1
	•	Method: GET
### 4.	Create a Location
	•	URL: http://localhost:8000/Locations
	•	Method: POST
	•	Body (JSON):

{
  "id": 1,
  "name": "Sample Location",
  "description": "A sample location",
  "encodingType": "application/vnd.geo+json",
  "location": {"type": "Point", "coordinates": [125.6, 10.1]}
}


### 5.	List Locations
	•	URL: http://localhost:8000/Locations
	•	Method: GET
### 6.	Get a Specific Location
	•	URL: http://localhost:8000/Locations/1
	•	Method: GET
### 7.	Create a Sensor
	•	URL: http://localhost:8000/Sensors
	•	Method: POST
	•	Body (JSON):

{
  "id": 1,
  "name": "Temperature Sensor",
  "description": "A sample sensor",
  "encodingType": "application/json",
  "metadata": "sensor metadata"
}


### 8.	List Sensors
	•	URL: http://localhost:8000/Sensors
	•	Method: GET
### 9.	Get a Specific Sensor
	•	URL: http://localhost:8000/Sensors/1
	•	Method: GET
### 10.	Create an ObservedProperty
	•	URL: http://localhost:8000/ObservedProperties
	•	Method: POST
	•	Body (JSON):

{
  "id": 1,
  "name": "Temperature",
  "description": "Temperature observed",
  "definition": "http://unitsofmeasure.org/ucum.html#para-30"
}


### 11.	List ObservedProperties
	•	URL: http://localhost:8000/ObservedProperties
	•	Method: GET
### 12.	Get a Specific ObservedProperty
	•	URL: http://localhost:8000/ObservedProperties/1
	•	Method: GET
### 13.	Create a Datastream
	•	URL: http://localhost:8000/Datastreams
	•	Method: POST
	•	Body (JSON):

{
  "id": 1,
  "name": "Temperature Datastream",
  "description": "Datastream for temperature",
  "observationType": "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement",
  "unitOfMeasurement": {
    "name": "degree Celsius",
    "symbol": "°C",
    "definition": "http://unitsofmeasure.org/ucum.html#para-30"
  },
  "thing_id": 1,
  "sensor_id": 1,
  "observed_property_id": 1
}


### 14.	List Datastreams
	•	URL: http://localhost:8000/Datastreams
	•	Method: GET
### 15.	Get a Specific Datastream
	•	URL: http://localhost:8000/Datastreams/1
	•	Method: GET
### 16.	Create an Observation
	•	URL: http://localhost:8000/Observations
	•	Method: POST
	•	Body (JSON):

{
  "id": 1,
  "phenomenonTime": "2025-03-25T12:00:00Z",
  "resultTime": "2025-03-25T12:00:00Z",
  "result": 23.5,
  "datastream_id": 1
}


### 17.	List Observations
	•	URL: http://localhost:8000/Observations
	•	Method: GET
### 18.	Get a Specific Observation
	•	URL: http://localhost:8000/Observations/1
	•	Method: GET
### 19.	Create a FeatureOfInterest
	•	URL: http://localhost:8000/FeaturesOfInterest
	•	Method: POST
	•	Body (JSON):

{
  "id": 1,
  "name": "Area of Interest",
  "description": "A specific region",
  "encodingType": "application/vnd.geo+json",
  "feature": {
    "type": "Polygon",
    "coordinates": [[[30, 10], [40, 40], [20, 40], [10, 20], [30, 10]]]
  }
}


### 20.	List FeaturesOfInterest
	•	URL: http://localhost:8000/FeaturesOfInterest
	•	Method: GET
### 21.	Get a Specific FeatureOfInterest
	•	URL: http://localhost:8000/FeaturesOfInterest/1
	•	Method: GET

## Tasking Endpoints
### 22.	Create an Actuator
	•	URL: http://localhost:8000/Actuators
	•	Method: POST
	•	Body (JSON):

{
  "id": 1,
  "name": "Valve Actuator",
  "description": "Controls a valve",
  "encodingType": "application/json",
  "metadata": "actuator metadata"
}


### 23.	List Actuators
	•	URL: http://localhost:8000/Actuators
	•	Method: GET
### 24.	Get a Specific Actuator
	•	URL: http://localhost:8000/Actuators/1
	•	Method: GET
### 25.	Create a TaskingCapability
	•	URL: http://localhost:8000/TaskingCapabilities
	•	Method: POST
	•	Body (JSON):

{
  "id": 1,
  "name": "Valve Control",
  "description": "Capability to control valve",
  "actuator_id": 1
}


### 26.	List TaskingCapabilities
	•	URL: http://localhost:8000/TaskingCapabilities
	•	Method: GET
### 27.	Get a Specific TaskingCapability
	•	URL: http://localhost:8000/TaskingCapabilities/1
	•	Method: GET
### 28.	Create a Task
	•	URL: http://localhost:8000/Tasks
	•	Method: POST
	•	Body (JSON):

{
  "id": 1,
  "taskingCapability_id": 1,
  "command": "Open Valve",
  "parameters": {"duration": 10},
  "status": "pending"
}


### 29.	List Tasks
	•	URL: http://localhost:8000/Tasks
	•	Method: GET
### 30.	Get a Specific Task
	•	URL: http://localhost:8000/Tasks/1
	•	Method: GET
