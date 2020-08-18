from sqlalchemy import create_engine, MetaData, insert, select, update
from sqlalchemy.orm import sessionmaker, load_only
from db import Base, Hub_Person, Hub_Location, Hub_Object, Person_Location_Link, Person_Object_Link, Object_Location_Link, Sat_Person_Patient_Details, Sat_Location_Patient_Address, Sat_Object_Patient_Operations, Sat_Person_Doctors_Names, Patient, Operations, Patient_Operations, Doctors

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

patient_csv = pd.read_csv('./csvs/patient.csv')
print(patient_csv)

operations_csv = pd.read_csv('./csvs/operations.csv')
print(operations_csv)

doctors_csv = pd.read_csv('./csvs/doctors.csv')
print(doctors_csv)

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


def get_link_table_value_to_insert(hub):
  return hub[4:] + "_id"



### Inserting the table

ref_id = 0
source_table = get_class_by_tablename(patient_csv.iloc[0].table)
print("SOURCE TABLE: {}".format(source_table))

query = select([source_table])
print("QUERY: {}".format(query))
data_to_copy = pd.read_sql_query(query, engine)

print("DATA: {}".format(data_to_copy))
for row, value in patient_csv.iterrows():
  columns = value['columns']
  columns = columns.split('::')
  destination = value['destination']
  hub = value['hub']
  keys = value['keys']
  keys = keys.split('::')
  links = value['links']
  links = links.split('::')

  transport_object = {
    'columns': columns,
    'destination': destination,
    'hub': hub,
    'keys': keys,
    'links': links
  }


  # print("TRANSPORT_OBJECT: {}".format(transport_object))

  # destination_table = get_class_by_tablename(transport_object['destination'])
  # print("DESTINATION: {}".format(destination_table))
  # destination_hub = get_class_by_tablename(transport_object['hub'])
  # print("DESTINATION HUB: {}".format(destination_hub))

  # for row, value in data_to_copy.iterrows():
    
  #   keys_to_add = {}
  #   for key in keys:
  #     keys_to_add.update({key: value[key]})
  #   key_query = insert(destination_hub).values(keys_to_add)
  #   key_result = engine.execute(key_query)
  #   hub_result = key_result.returned_defaults.values()[0]
  #   print("HUB RESULT: {}".format(key_result.returned_defaults.values()[0]))


  #   values_to_add = {'hub_id': hub_result}
  #   for column in columns:
  #     values_to_add.update({column: value[column]})

  #   print("VALUES TO ADD: {}".format(values_to_add))
  #   value_query = insert(destination_table).values(values_to_add)
  #   result = engine.execute(value_query)
  #   print("RESULT: {}".format(result))
  #   print("RESULT METHODS: {}".format(dir(result)))







