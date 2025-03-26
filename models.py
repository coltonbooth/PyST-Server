from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel

Base = declarative_base()

# SQLAlchemy Models
class Thing(Base):
    __tablename__ = "things"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    encodingType = Column(String)
    location = Column(JSON)

class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    encodingType = Column(String)
    metadata_ = Column(String, nullable=True)

class ObservedProperty(Base):
    __tablename__ = "observed_properties"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    definition = Column(String, nullable=True)

class Datastream(Base):
    __tablename__ = "datastreams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    observationType = Column(String)
    unitOfMeasurement = Column(JSON)
    thing_id = Column(Integer, ForeignKey("things.id"))
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    observed_property_id = Column(Integer, ForeignKey("observed_properties.id"))
    thing = relationship("Thing")
    sensor = relationship("Sensor")
    observed_property = relationship("ObservedProperty")

class Observation(Base):
    __tablename__ = "observations"
    id = Column(Integer, primary_key=True, index=True)
    phenomenonTime = Column(DateTime)
    resultTime = Column(DateTime)
    result = Column(Float)
    datastream_id = Column(Integer, ForeignKey("datastreams.id"))
    datastream = relationship("Datastream")

class FeatureOfInterest(Base):
    __tablename__ = "features_of_interest"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    encodingType = Column(String)
    feature = Column(JSON)

class Actuator(Base):
    __tablename__ = "actuators"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    encodingType = Column(String)
    metadata_ = Column(String, nullable=True)

class TaskingCapability(Base):
    __tablename__ = "tasking_capabilities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    actuator_id = Column(Integer, ForeignKey("actuators.id"))
    actuator = relationship("Actuator")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    taskingCapability_id = Column(Integer, ForeignKey("tasking_capabilities.id"))
    command = Column(String)
    parameters = Column(JSON)
    status = Column(String, default="pending")
    createdAt = Column(DateTime, default=datetime.now)
    tasking_capability = relationship("TaskingCapability")

# Pydantic Schemas
class ThingSchema(BaseModel):
    id: int
    name: str
    description: str = None
    class Config:
        orm_mode = True

class LocationSchema(BaseModel):
    id: int
    name: str
    description: str = None
    encodingType: str
    location: dict
    class Config:
        orm_mode = True

class SensorSchema(BaseModel):
    id: int
    name: str
    description: str = None
    encodingType: str
    metadata_: str = None
    class Config:
        orm_mode = True

class ObservedPropertySchema(BaseModel):
    id: int
    name: str
    description: str = None
    definition: str = None
    class Config:
        orm_mode = True

class DatastreamSchema(BaseModel):
    id: int
    name: str
    description: str = None
    observationType: str
    unitOfMeasurement: dict
    thing_id: int
    sensor_id: int
    observed_property_id: int
    class Config:
        orm_mode = True

class ObservationSchema(BaseModel):
    id: int
    phenomenonTime: datetime
    resultTime: datetime
    result: float
    datastream_id: int
    class Config:
        orm_mode = True

class FeatureOfInterestSchema(BaseModel):
    id: int
    name: str
    description: str = None
    encodingType: str
    feature: dict
    class Config:
        orm_mode = True

class ActuatorSchema(BaseModel):
    id: int
    name: str
    description: str = None
    encodingType: str
    metadata_: str = None
    class Config:
        orm_mode = True

class TaskingCapabilitySchema(BaseModel):
    id: int
    name: str
    description: str = None
    actuator_id: int
    class Config:
        orm_mode = True

class TaskSchema(BaseModel):
    id: int
    taskingCapability_id: int
    command: str
    parameters: dict
    status: str = "pending"
    createdAt: datetime
    class Config:
        orm_mode = True
