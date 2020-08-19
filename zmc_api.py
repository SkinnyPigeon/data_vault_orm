from sqlalchemy import create_engine, MetaData, insert, select, update
from sqlalchemy.orm import sessionmaker, load_only
from db import Base, Hub_Person, Hub_Location, Hub_Object, Person_Location_Link, Person_Object_Link, Object_Location_Link, Sat_Person_Patient_Details, Sat_Location_Patient_Address, Sat_Object_Patient_Operations, Sat_Person_Doctors_Names, Sat_Person_Test_Doctors, Sat_Person_Test_Patients, Sat_Object_Test_Details, Sat_Location_Test_Address, Patient, Operations, Patient_Operations, Doctors, Tests

import pandas as pd

import os
from dotenv import load_dotenv
from pathlib import Path

project_folder = os.path.expanduser('~/code/dv_testing/')
load_dotenv(os.path.join(project_folder, '.env'))
PASSWORD = os.getenv('PASSWORD')

from control_files.zmc.zmc_patient_appointments import zmc_patient_appointments_hubs, zmc_patient_appointments_links, zmc_patient_appointments_satellites
from control_files.zmc.zmc_patient_details import zmc_patient_details_hubs, zmc_patient_details_links, zmc_patient_details_satellites
from control_files.zmc.zmc_patient_documents import zmc_patient_documents_hubs, zmc_patient_documents_links, zmc_patient_documents_satellites
from control_files.zmc.zmc_patient_measurements import zmc_patient_measurements_hubs, zmc_patient_measurements_links, zmc_patient_measurements_satellites
from control_files.zmc.zmc_patient_operations import zmc_patient_operations_hubs, zmc_patient_operations_links, zmc_patient_operations_satellites
from control_files.zmc.zmc_wearable import zmc_wearable_hubs, zmc_wearable_links, zmc_wearable_satellites

engine = create_engine('postgresql://postgres:{}@localhost:5434/testing_v4'.format(PASSWORD), echo='debug')

con = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

### Helper functions

def get_class_by_tablename(table_fullname):
  for class_name in Base._decl_class_registry.values():
    if hasattr(class_name, '__table__') and class_name.__table__.fullname == table_fullname:
      return class_name


def get_link_table_value_to_insert(hub):
  return hub[4:] + "_id"

def control_picker(class_name):
  if class_name == 'appointments':
    return zmc_patient_appointments_hubs, zmc_patient_appointments_links, zmc_patient_appointments_satellites
  elif class_name == 'details':
    return zmc_patient_details_hubs, zmc_patient_details_links, zmc_patient_details_satellites
  elif class_name == 'documents':
    return zmc_patient_documents_hubs, zmc_patient_documents_links, zmc_patient_documents_satellites
  elif class_name == 'measurements':
    return zmc_patient_measurements_hubs, zmc_patient_measurements_links, zmc_patient_measurements_satellites
  elif class_name == 'operations':
    return zmc_patient_operations_hubs, zmc_patient_operations_links, zmc_patient_operations_satellites
  elif class_name == 'wearable':
    return zmc_wearable_hubs, zmc_wearable_links, zmc_wearable_satellites


### Inserting the table

hubs, links, satellites = control_picker('doctors')

source_table = get_class_by_tablename(hubs['table'])
print("SOURCE TABLE: {}".format(source_table))

query = select([source_table])
print("QUERY: {}".format(query))
data_to_copy = pd.read_sql_query(query, engine)

print("DATA: {}".format(data_to_copy))

# for row in data_to_copy.itertuples(index=False):
#   for hub in hubs['hubs']:
#     print("HUB: {}".format(hub))
#     keys_to_insert = {}
#     for key in hub['keys']:
#       try:
#         keys_to_insert.update({key: getattr(row, key)})
#       except:
#         print("Wrong Key but don't worry")

#     hub_to_insert = get_class_by_tablename(hub['hub'])
    
#     hub_query = insert(hub_to_insert).values(keys_to_insert)
#     hub_result = engine.execute(hub_query, con=engine)

#     hub_id = hub_result.returned_defaults[0]

#     print("HUB NAME: {}".format(hub['hub']))
#     print("HUB ID: {}".format(hub_id))

#     for satellite in satellites['satellites']:
#       if satellite['hub'] == hub['hub']:
#         satellite_to_insert = get_class_by_tablename(satellite['satellite'])
#         # print(satellite_to_insert)
#         columns_to_insert = {'hub_id': hub_id}
#         for column in satellite['columns']:
#           try:
#             columns_to_insert.update({column: getattr(row, column)})
#           except:
#             print("Error")

#         satellite_query = insert(satellite_to_insert).values(columns_to_insert)
#         satellite_result = engine.execute(satellite_query, con=engine)

#     id_name = get_link_table_value_to_insert(hub['hub'])
#     print("ID NAME: {}".format(id_name))
#     for link in links['links']:
#       print("LINK BEFORE: {}".format(link))

#       for value in link['values']:
#         if value == id_name:
#           link['values'][value] = hub_id
#           print("LINK AFTER: {}".format(link))

#   for link in links['links']:
#     link_to_insert = get_class_by_tablename(link['link'])
#     ids_to_insert = link['values']
#     link_query = insert(link_to_insert).values(ids_to_insert)
#     link_result = engine.execute(link_query, con=engine)

