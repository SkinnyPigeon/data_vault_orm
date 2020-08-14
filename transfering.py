from sqlalchemy import create_engine, MetaData
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