from sqlalchemy import create_engine, MetaData, insert
from sqlalchemy.orm import sessionmaker, load_only
from db import Base, Patient, Hub_Person, Hub_Location, Person_Location_Link, Sat_Location_Patient_Address, Sat_Person_Patient_Details
import pandas as pd

import os
from dotenv import load_dotenv
from pathlib import Path

project_folder = os.path.expanduser('~/code/dv_testing/')
load_dotenv(os.path.join(project_folder, '.env'))
PASSWORD = os.getenv('PASSWORD')

engine = create_engine('postgresql://postgres:{}@localhost:5434/testing_v6'.format(PASSWORD), echo='debug')

con = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Patient).filter(Patient.serums_id == 1)
print(query.all())

df = pd.read_sql(query.statement, con=con)
print(df)

patient_csv = pd.read_csv('./patient.csv')
print(patient_csv)

operations_csv = pd.read_csv('./operations.csv')
print(operations_csv)

doctors_csv = pd.read_csv('./doctors.csv')
print(doctors_csv)

for row, value in patient_csv.iterrows():
  table = value['table']
  column = value['column']
  destination = value['destination']
  hub = value['hub']
  keys = value['keys']
  keys = keys.split('::')
  links = value['links']
  links = links.split('::')

  transport_object = {
    'table': table,
    'column': column,
    'destination': destination,
    'hub': hub,
    'keys': keys,
    'links': links
  }

  print(transport_object)



### Helper functions

def get_hub(destination_table):
    if "sat_person_" in destination_table:
        return "hub_person"
    elif "sat_location_" in destination_table:
        return "hub_location"

def get_class_by_tablename(table_fullname):
  for class_name in Base._decl_class_registry.values():
    if hasattr(class_name, '__table__') and class_name.__table__.fullname == table_fullname:
      return class_name

def insert_record(class_name):
    print(class_name)