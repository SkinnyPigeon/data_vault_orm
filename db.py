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


### DV Tables

class Hub_Person(Base):
    __tablename__ = 'hub_person'
    id = Column(Integer, primary_key=True)
    serums_id = Column(Integer)
    doctors_id = Column(Integer)

class Hub_Location(Base):
    __tablename__ = 'hub_location'
    id = Column(Integer, primary_key=True)
    serums_id = Column(Integer)
    hospital_id = Column(Integer)

class Hub_Object(Base):
    __tablename__ = 'hub_object'
    id = Column(Integer, primary_key=True)
    serums_id = Column(Integer)
    operations_id = Column(Integer)
    test_id = Column(Integer)

class Person_Location_Link(Base):
    __tablename__ = 'person_location_link'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey(Hub_Person.id))
    location_id = Column(Integer, ForeignKey(Hub_Location.id))

class Person_Object_Link(Base):
    __tablename__ = 'person_object_link'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey(Hub_Person.id))
    object_id = Column(Integer, ForeignKey(Hub_Object.id))

class Object_Location_Link(Base):
    __tablename__ = 'object_location_link'
    id = Column(Integer, primary_key=True)
    object_id = Column(Integer, ForeignKey(Hub_Object.id))
    location_id = Column(Integer, ForeignKey(Hub_Location.id))

class Sat_Person_Patient_Details(Base):
    __tablename__ = 'sat_person_patient_details'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    hub_id = Column(Integer, ForeignKey(Hub_Person.id))

class Sat_Location_Patient_Address(Base):
    __tablename__ = 'sat_location_patient_address'
    id = Column(Integer, primary_key=True)
    address = Column(String)
    postcode = Column(String)
    hub_id = Column(Integer, ForeignKey(Hub_Location.id))

class Sat_Object_Patient_Operations(Base):
    __tablename__ = 'sat_object_patient_operations'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    hub_id = Column(Integer, ForeignKey(Hub_Object.id)) 

class Sat_Person_Doctors_Names(Base):
    __tablename__ = 'sat_person_doctors_names'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hub_id = Column(Integer, ForeignKey(Hub_Person.id))

class Sat_Person_Test_Doctors(Base):
    __tablename__ = 'sat_person_test_doctors'
    id = Column(Integer, primary_key=True)
    doctors_name = Column(String)
    hub_id = Column(Integer, ForeignKey(Hub_Person.id))

class Sat_Person_Test_Patients(Base):
    __tablename__ = 'sat_person_test_patients'
    id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    hub_id = Column(Integer, ForeignKey(Hub_Person.id))

class Sat_Object_Test_Details(Base):
    __tablename__ = 'sat_object_test_details'
    id = Column(Integer, primary_key=True)
    test_name = Column(String)
    hub_id = Column(Integer, ForeignKey(Hub_Object.id)) 

class Sat_Location_Test_Address(Base):
    __tablename__ = 'sat_location_hospital_address'
    id = Column(Integer, primary_key=True)
    hospital_address = Column(String)
    hospital_postcode = Column(String)
    hub_id = Column(Integer, ForeignKey(Hub_Location.id))


### Source tables

class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    serums_id = Column(Integer)
    name = Column(String)
    age = Column(Integer)
    address = Column(String)
    postcode = Column(String)

class Operations(Base):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True)
    serums_id = Column(Integer)
    operation_id = Column(Integer)
    description = Column(String)

class Patient_Operations(Base):
    __tablename__ = 'patient_operations'
    patient_id = Column(Integer, ForeignKey(Patient.id), primary_key=True)
    operations_id = Column(Integer, ForeignKey(Operations.id), primary_key=True)

class Doctors(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    doctors_id = Column(Integer)
    name = Column(String)

class Tests(Base):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    serums_id = Column(Integer)
    test_name = Column(String)
    test_id = Column(Integer)
    hospital_address = Column(String)
    hospital_postcode = Column(String)
    hospital_id = Column(Integer)
    doctors_name = Column(String)
    doctors_id = Column(Integer)

Base.metadata.create_all(engine)