from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="SensorThings API - Sensing and Tasking")

things_db = {}
locations_db = {}
sensors_db = {}
observed_properties_db = {}
datastreams_db = {}
observations_db = {}
features_db = {}

actuators_db = {}
tasking_capabilities_db = {}
tasks_db = {}

class Thing(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

class Location(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    encodingType: str
    location: dict

class Sensor(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    encodingType: str
    metadata: Optional[str] = None

class ObservedProperty(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    definition: Optional[str] = None

class Datastream(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    observationType: str
    unitOfMeasurement: dict
    thing_id: int
    sensor_id: int
    observed_property_id: int

class Observation(BaseModel):
    id: int
    phenomenonTime: datetime
    resultTime: datetime
    result: float
    datastream_id: int

class FeatureOfInterest(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    encodingType: str
    feature: dict

class Actuator(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    encodingType: str
    metadata: Optional[str] = None

class TaskingCapability(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    actuator_id: int

class Task(BaseModel):
    id: int
    taskingCapability_id: int
    command: str
    parameters: dict
    status: Optional[str] = "pending"
    createdAt: datetime = datetime.now()

@app.post("/Things", response_model=Thing)
def create_thing(thing: Thing):
    if thing.id in things_db:
        raise HTTPException(status_code=400, detail="Thing already exists")
    things_db[thing.id] = thing
    return thing

@app.get("/Things", response_model=List[Thing])
def list_things():
    return list(things_db.values())

@app.get("/Things/{thing_id}", response_model=Thing)
def get_thing(thing_id: int):
    if thing_id not in things_db:
        raise HTTPException(status_code=404, detail="Thing not found")
    return things_db[thing_id]

@app.post("/Locations", response_model=Location)
def create_location(location: Location):
    if location.id in locations_db:
        raise HTTPException(status_code=400, detail="Location already exists")
    locations_db[location.id] = location
    return location

@app.get("/Locations", response_model=List[Location])
def list_locations():
    return list(locations_db.values())

@app.get("/Locations/{location_id}", response_model=Location)
def get_location(location_id: int):
    if location_id not in locations_db:
        raise HTTPException(status_code=404, detail="Location not found")
    return locations_db[location_id]

@app.post("/Sensors", response_model=Sensor)
def create_sensor(sensor: Sensor):
    if sensor.id in sensors_db:
        raise HTTPException(status_code=400, detail="Sensor already exists")
    sensors_db[sensor.id] = sensor
    return sensor

@app.get("/Sensors", response_model=List[Sensor])
def list_sensors():
    return list(sensors_db.values())

@app.get("/Sensors/{sensor_id}", response_model=Sensor)
def get_sensor(sensor_id: int):
    if sensor_id not in sensors_db:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensors_db[sensor_id]

@app.post("/ObservedProperties", response_model=ObservedProperty)
def create_observed_property(observed_property: ObservedProperty):
    if observed_property.id in observed_properties_db:
        raise HTTPException(status_code=400, detail="ObservedProperty already exists")
    observed_properties_db[observed_property.id] = observed_property
    return observed_property

@app.get("/ObservedProperties", response_model=List[ObservedProperty])
def list_observed_properties():
    return list(observed_properties_db.values())

@app.get("/ObservedProperties/{observed_property_id}", response_model=ObservedProperty)
def get_observed_property(observed_property_id: int):
    if observed_property_id not in observed_properties_db:
        raise HTTPException(status_code=404, detail="ObservedProperty not found")
    return observed_properties_db[observed_property_id]

@app.post("/Datastreams", response_model=Datastream)
def create_datastream(datastream: Datastream):
    if datastream.id in datastreams_db:
        raise HTTPException(status_code=400, detail="Datastream already exists")
    if datastream.thing_id not in things_db:
        raise HTTPException(status_code=400, detail="Referenced Thing does not exist")
    if datastream.sensor_id not in sensors_db:
        raise HTTPException(status_code=400, detail="Referenced Sensor does not exist")
    if datastream.observed_property_id not in observed_properties_db:
        raise HTTPException(status_code=400, detail="Referenced ObservedProperty does not exist")
    datastreams_db[datastream.id] = datastream
    return datastream

@app.get("/Datastreams", response_model=List[Datastream])
def list_datastreams():
    return list(datastreams_db.values())

@app.get("/Datastreams/{datastream_id}", response_model=Datastream)
def get_datastream(datastream_id: int):
    if datastream_id not in datastreams_db:
        raise HTTPException(status_code=404, detail="Datastream not found")
    return datastreams_db[datastream_id]

@app.post("/Observations", response_model=Observation)
def create_observation(observation: Observation):
    if observation.id in observations_db:
        raise HTTPException(status_code=400, detail="Observation already exists")
    if observation.datastream_id not in datastreams_db:
        raise HTTPException(status_code=400, detail="Referenced Datastream does not exist")
    observations_db[observation.id] = observation
    return observation

@app.get("/Observations", response_model=List[Observation])
def list_observations():
    return list(observations_db.values())

@app.get("/Observations/{observation_id}", response_model=Observation)
def get_observation(observation_id: int):
    if observation_id not in observations_db:
        raise HTTPException(status_code=404, detail="Observation not found")
    return observations_db[observation_id]

@app.post("/FeaturesOfInterest", response_model=FeatureOfInterest)
def create_feature(feature: FeatureOfInterest):
    if feature.id in features_db:
        raise HTTPException(status_code=400, detail="FeatureOfInterest already exists")
    features_db[feature.id] = feature
    return feature

@app.get("/FeaturesOfInterest", response_model=List[FeatureOfInterest])
def list_features():
    return list(features_db.values())

@app.get("/FeaturesOfInterest/{feature_id}", response_model=FeatureOfInterest)
def get_feature(feature_id: int):
    if feature_id not in features_db:
        raise HTTPException(status_code=404, detail="FeatureOfInterest not found")
    return features_db[feature_id]

@app.post("/Actuators", response_model=Actuator)
def create_actuator(actuator: Actuator):
    if actuator.id in actuators_db:
        raise HTTPException(status_code=400, detail="Actuator already exists")
    actuators_db[actuator.id] = actuator
    return actuator

@app.get("/Actuators", response_model=List[Actuator])
def list_actuators():
    return list(actuators_db.values())

@app.get("/Actuators/{actuator_id}", response_model=Actuator)
def get_actuator(actuator_id: int):
    if actuator_id not in actuators_db:
        raise HTTPException(status_code=404, detail="Actuator not found")
    return actuators_db[actuator_id]

@app.post("/TaskingCapabilities", response_model=TaskingCapability)
def create_tasking_capability(capability: TaskingCapability):
    if capability.id in tasking_capabilities_db:
        raise HTTPException(status_code=400, detail="TaskingCapability already exists")
    if capability.actuator_id not in actuators_db:
        raise HTTPException(status_code=400, detail="Referenced Actuator does not exist")
    tasking_capabilities_db[capability.id] = capability
    return capability

@app.get("/TaskingCapabilities", response_model=List[TaskingCapability])
def list_tasking_capabilities():
    return list(tasking_capabilities_db.values())

@app.get("/TaskingCapabilities/{capability_id}", response_model=TaskingCapability)
def get_tasking_capability(capability_id: int):
    if capability_id not in tasking_capabilities_db:
        raise HTTPException(status_code=404, detail="TaskingCapability not found")
    return tasking_capabilities_db[capability_id]

@app.post("/Tasks", response_model=Task)
def create_task(task: Task):
    if task.id in tasks_db:
        raise HTTPException(status_code=400, detail="Task already exists")
    if task.taskingCapability_id not in tasking_capabilities_db:
        raise HTTPException(status_code=400, detail="Referenced TaskingCapability does not exist")
    tasks_db[task.id] = task
    return task

@app.get("/Tasks", response_model=List[Task])
def list_tasks():
    return list(tasks_db.values())

@app.get("/Tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)