from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
from pathlib import Path

project_folder = os.path.expanduser('~/code/dv_testing/')
load_dotenv(os.path.join(project_folder, '.env'))
PASSWORD = os.getenv('PASSWORD')

engine = create_engine('postgresql://postgres:{}@localhost:5434/testing_v6'.format(PASSWORD), echo='debug')



class Hub_Person(Base):
    __tablename__ = 'hub_person'
    id = Column(Integer, primary_key=True)
    serums_id = Column(Integer)

class Hub_Location(Base):
    __tablename__ = 'hub_location'
    id = Column(Integer, primary_key=True)
    serums_id = Column(Integer)

class Person_Location_Link(Base):
    __tablename__ = 'person_location_link'
    person_id = Column(Integer, ForeignKey(Hub_Person.id), primary_key=True)
    location_id = Column(Integer, ForeignKey(Hub_Location.id), primary_key=True)

class Sat_Person_Patient_Details(Base):
    __tablename__ = 'sat_person_patient_details'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    hub_id = Column(Integer, ForeignKey(Hub_Person.id))

class Sat_Location_Patient_Address(Base):
    __tablename__ = 'sat_location_patient_address'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    hub_id = Column(Integer, ForeignKey(Hub_Location.id))

class Patient(Base):
    __tablename__ = 'patient'
    serums_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer, primary_key=True)
    address = Column(String)
    postcode = Column(String)

Base.metadata.create_all(engine)