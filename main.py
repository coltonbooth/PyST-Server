import logging
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn
from datetime import datetime
from db import SessionLocal, engine
import models
from models import (
    ThingSchema, LocationSchema, SensorSchema, ObservedPropertySchema,
    DatastreamSchema, ObservationSchema, FeatureOfInterestSchema,
    ActuatorSchema, TaskingCapabilitySchema, TaskSchema
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SensorThings API - Sensing and Tasking")

# Enable CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API router with versioning
router = APIRouter(prefix="/v1", tags=["SensorThings"])

@router.post("/Things", response_model=ThingSchema)
def create_thing(thing: ThingSchema, db: Session = Depends(get_db)):
    db_thing = db.query(models.Thing).filter(models.Thing.id == thing.id).first()
    if db_thing:
        logger.warning("Thing already exists: %s", thing.id)
        raise HTTPException(status_code=400, detail="Thing already exists")
    new_thing = models.Thing(**thing.dict())
    db.add(new_thing)
    db.commit()
    db.refresh(new_thing)
    return new_thing

@router.get("/Things", response_model=list[ThingSchema])
def list_things(db: Session = Depends(get_db)):
    return db.query(models.Thing).all()

@router.get("/Things/{thing_id}", response_model=ThingSchema)
def get_thing(thing_id: int, db: Session = Depends(get_db)):
    db_thing = db.query(models.Thing).filter(models.Thing.id == thing_id).first()
    if not db_thing:
        raise HTTPException(status_code=404, detail="Thing not found")
    return db_thing

@router.post("/Locations", response_model=LocationSchema)
def create_location(location: LocationSchema, db: Session = Depends(get_db)):
    db_location = db.query(models.Location).filter(models.Location.id == location.id).first()
    if db_location:
        logger.warning("Location already exists: %s", location.id)
        raise HTTPException(status_code=400, detail="Location already exists")
    new_location = models.Location(**location.dict())
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location

@router.get("/Locations", response_model=list[LocationSchema])
def list_locations(db: Session = Depends(get_db)):
    return db.query(models.Location).all()

@router.get("/Locations/{location_id}", response_model=LocationSchema)
def get_location(location_id: int, db: Session = Depends(get_db)):
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location

@router.post("/Sensors", response_model=SensorSchema)
def create_sensor(sensor: SensorSchema, db: Session = Depends(get_db)):
    db_sensor = db.query(models.Sensor).filter(models.Sensor.id == sensor.id).first()
    if db_sensor:
        logger.warning("Sensor already exists: %s", sensor.id)
        raise HTTPException(status_code=400, detail="Sensor already exists")
    new_sensor = models.Sensor(**sensor.dict())
    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)
    return new_sensor

@router.get("/Sensors", response_model=list[SensorSchema])
def list_sensors(db: Session = Depends(get_db)):
    return db.query(models.Sensor).all()

@router.get("/Sensors/{sensor_id}", response_model=SensorSchema)
def get_sensor(sensor_id: int, db: Session = Depends(get_db)):
    db_sensor = db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()
    if not db_sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return db_sensor

@router.post("/ObservedProperties", response_model=ObservedPropertySchema)
def create_observed_property(observed_property: ObservedPropertySchema, db: Session = Depends(get_db)):
    db_op = db.query(models.ObservedProperty).filter(models.ObservedProperty.id == observed_property.id).first()
    if db_op:
        logger.warning("ObservedProperty already exists: %s", observed_property.id)
        raise HTTPException(status_code=400, detail="ObservedProperty already exists")
    new_op = models.ObservedProperty(**observed_property.dict())
    db.add(new_op)
    db.commit()
    db.refresh(new_op)
    return new_op

@router.get("/ObservedProperties", response_model=list[ObservedPropertySchema])
def list_observed_properties(db: Session = Depends(get_db)):
    return db.query(models.ObservedProperty).all()

@router.get("/ObservedProperties/{observed_property_id}", response_model=ObservedPropertySchema)
def get_observed_property(observed_property_id: int, db: Session = Depends(get_db)):
    db_op = db.query(models.ObservedProperty).filter(models.ObservedProperty.id == observed_property_id).first()
    if not db_op:
        raise HTTPException(status_code=404, detail="ObservedProperty not found")
    return db_op

@router.post("/Datastreams", response_model=DatastreamSchema)
def create_datastream(datastream: DatastreamSchema, db: Session = Depends(get_db)):
    db_ds = db.query(models.Datastream).filter(models.Datastream.id == datastream.id).first()
    if db_ds:
        logger.warning("Datastream already exists: %s", datastream.id)
        raise HTTPException(status_code=400, detail="Datastream already exists")
    if not db.query(models.Thing).filter(models.Thing.id == datastream.thing_id).first():
        raise HTTPException(status_code=400, detail="Referenced Thing does not exist")
    if not db.query(models.Sensor).filter(models.Sensor.id == datastream.sensor_id).first():
        raise HTTPException(status_code=400, detail="Referenced Sensor does not exist")
    if not db.query(models.ObservedProperty).filter(models.ObservedProperty.id == datastream.observed_property_id).first():
        raise HTTPException(status_code=400, detail="Referenced ObservedProperty does not exist")
    new_ds = models.Datastream(**datastream.dict())
    db.add(new_ds)
    db.commit()
    db.refresh(new_ds)
    return new_ds

@router.get("/Datastreams", response_model=list[DatastreamSchema])
def list_datastreams(db: Session = Depends(get_db)):
    return db.query(models.Datastream).all()

@router.get("/Datastreams/{datastream_id}", response_model=DatastreamSchema)
def get_datastream(datastream_id: int, db: Session = Depends(get_db)):
    db_ds = db.query(models.Datastream).filter(models.Datastream.id == datastream_id).first()
    if not db_ds:
        raise HTTPException(status_code=404, detail="Datastream not found")
    return db_ds

@router.post("/Observations", response_model=ObservationSchema)
def create_observation(observation: ObservationSchema, db: Session = Depends(get_db)):
    db_obs = db.query(models.Observation).filter(models.Observation.id == observation.id).first()
    if db_obs:
        logger.warning("Observation already exists: %s", observation.id)
        raise HTTPException(status_code=400, detail="Observation already exists")
    if not db.query(models.Datastream).filter(models.Datastream.id == observation.datastream_id).first():
        raise HTTPException(status_code=400, detail="Referenced Datastream does not exist")
    new_obs = models.Observation(**observation.dict())
    db.add(new_obs)
    db.commit()
    db.refresh(new_obs)
    return new_obs

@router.get("/Observations", response_model=list[ObservationSchema])
def list_observations(db: Session = Depends(get_db)):
    return db.query(models.Observation).all()

@router.get("/Observations/{observation_id}", response_model=ObservationSchema)
def get_observation(observation_id: int, db: Session = Depends(get_db)):
    db_obs = db.query(models.Observation).filter(models.Observation.id == observation_id).first()
    if not db_obs:
        raise HTTPException(status_code=404, detail="Observation not found")
    return db_obs

@router.post("/FeaturesOfInterest", response_model=FeatureOfInterestSchema)
def create_feature(feature: FeatureOfInterestSchema, db: Session = Depends(get_db)):
    db_feature = db.query(models.FeatureOfInterest).filter(models.FeatureOfInterest.id == feature.id).first()
    if db_feature:
        logger.warning("FeatureOfInterest already exists: %s", feature.id)
        raise HTTPException(status_code=400, detail="FeatureOfInterest already exists")
    new_feature = models.FeatureOfInterest(**feature.dict())
    db.add(new_feature)
    db.commit()
    db.refresh(new_feature)
    return new_feature

@router.get("/FeaturesOfInterest", response_model=list[FeatureOfInterestSchema])
def list_features(db: Session = Depends(get_db)):
    return db.query(models.FeatureOfInterest).all()

@router.get("/FeaturesOfInterest/{feature_id}", response_model=FeatureOfInterestSchema)
def get_feature(feature_id: int, db: Session = Depends(get_db)):
    db_feature = db.query(models.FeatureOfInterest).filter(models.FeatureOfInterest.id == feature_id).first()
    if not db_feature:
        raise HTTPException(status_code=404, detail="FeatureOfInterest not found")
    return db_feature

@router.post("/Actuators", response_model=ActuatorSchema)
def create_actuator(actuator: ActuatorSchema, db: Session = Depends(get_db)):
    db_act = db.query(models.Actuator).filter(models.Actuator.id == actuator.id).first()
    if db_act:
        logger.warning("Actuator already exists: %s", actuator.id)
        raise HTTPException(status_code=400, detail="Actuator already exists")
    new_act = models.Actuator(**actuator.dict())
    db.add(new_act)
    db.commit()
    db.refresh(new_act)
    return new_act

@router.get("/Actuators", response_model=list[ActuatorSchema])
def list_actuators(db: Session = Depends(get_db)):
    return db.query(models.Actuator).all()

@router.get("/Actuators/{actuator_id}", response_model=ActuatorSchema)
def get_actuator(actuator_id: int, db: Session = Depends(get_db)):
    db_act = db.query(models.Actuator).filter(models.Actuator.id == actuator_id).first()
    if not db_act:
        raise HTTPException(status_code=404, detail="Actuator not found")
    return db_act

@router.post("/TaskingCapabilities", response_model=TaskingCapabilitySchema)
def create_tasking_capability(capability: TaskingCapabilitySchema, db: Session = Depends(get_db)):
    db_cap = db.query(models.TaskingCapability).filter(models.TaskingCapability.id == capability.id).first()
    if db_cap:
        logger.warning("TaskingCapability already exists: %s", capability.id)
        raise HTTPException(status_code=400, detail="TaskingCapability already exists")
    if not db.query(models.Actuator).filter(models.Actuator.id == capability.actuator_id).first():
        raise HTTPException(status_code=400, detail="Referenced Actuator does not exist")
    new_cap = models.TaskingCapability(**capability.dict())
    db.add(new_cap)
    db.commit()
    db.refresh(new_cap)
    return new_cap

@router.get("/TaskingCapabilities", response_model=list[TaskingCapabilitySchema])
def list_tasking_capabilities(db: Session = Depends(get_db)):
    return db.query(models.TaskingCapability).all()

@router.get("/TaskingCapabilities/{capability_id}", response_model=TaskingCapabilitySchema)
def get_tasking_capability(capability_id: int, db: Session = Depends(get_db)):
    db_cap = db.query(models.TaskingCapability).filter(models.TaskingCapability.id == capability_id).first()
    if not db_cap:
        raise HTTPException(status_code=404, detail="TaskingCapability not found")
    return db_cap

@router.post("/Tasks", response_model=TaskSchema)
def create_task(task: TaskSchema, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task.id).first()
    if db_task:
        logger.warning("Task already exists: %s", task.id)
        raise HTTPException(status_code=400, detail="Task already exists")
    if not db.query(models.TaskingCapability).filter(models.TaskingCapability.id == task.taskingCapability_id).first():
        raise HTTPException(status_code=400, detail="Referenced TaskingCapability does not exist")
    new_task = models.Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/Tasks", response_model=list[TaskSchema])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@router.get("/Tasks/{task_id}", response_model=TaskSchema)
def get_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
