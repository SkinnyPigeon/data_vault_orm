# Imports
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, create_engine
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
from pathlib import Path

project_folder = os.path.expanduser('~/code/dv_testing/')
load_dotenv(os.path.join(project_folder, '.env'))
PASSWORD = os.getenv('PASSWORD')

engine = create_engine('postgresql://postgres:{}@localhost:5434/testing_v4'.format(PASSWORD), echo='debug')

# Tables/Classes

class ZMC_Wearable(Base):
    __tablename__ = 'wearable'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    day_nr = Column(Integer, primary_key=True)
    time_total = Column(Integer)
    time_passive = Column(Integer)
    time_active = Column(Integer)
    time_sit = Column(Integer)
    time_stand = Column(Integer)
    time_walk = Column(Integer)
    time_cycle = Column(Integer)
    time_hi = Column(Integer)
    nr_sst = Column(Integer)
    steps_total = Column(Integer)
    cadence = Column(Integer)
    cyc_rot = Column(Integer)
    cyc_rpm = Column(Integer)

class ZMC_Patient_Details(Base):
    __tablename__ = 'patient_details'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    gschl = Column(String)
    nname = Column(String)
    nnams = Column(String)
    vname = Column(String)
    titel = Column(String)
    namzu = Column(String)
    gbdat = Column(DateTime(timezone=False))
    gbnam = Column(String)
    gbnas = Column(String)
    gland = Column(String)
    natio = Column(String)
    land = Column(String)
    pstlz = Column(String)
    ort = Column(String)
    stras = Column(String)
    telf1 = Column(String)

class ZMC_Patient_Measurements(Base):
    __tablename__ = 'patient_measurements'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    height = Column(Integer)
    weight = Column(Integer)
    date = Column(DateTime(timezone=False))

class ZMC_Documents(Base):
    __tablename__ = 'patient_documents'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    report_title = Column(String, primary_key=True)
    department = Column(String)
    date = Column(DateTime(timezone=False))
    content = Column(Text)

class ZMC_Serums_IDs(Base):
    __tablename__ = 'serums_ids'
    __table_args__ = {'schema': 'zmc'}
    serums_id = Column(Integer, primary_key=True)
    patnr = Column(Integer, primary_key=True)

class ZMC_Patient_Rules(Base):
    __tablename__ = 'patient_rules'
    __table_args__ = {'schema': 'zmc'}
    rule_id = Column(Integer, primary_key=True)
    tags = Column(ARRAY(String))
    filters = Column(JSON)

class ZMC_Appointments(Base):
    __tablename__ = 'patient_appointments'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    type = Column(String, primary_key=True)
    date = Column(DateTime(timezone=False))
    notes = Column(Text)

class ZMC_Opperations(Base):
    __tablename__ = 'patient_opperations'
    __table_args__ = {'schema': 'zmc'}
    patnr = Column(Integer, primary_key=True)
    anatomical_location = Column(String)
    date = Column(DateTime(timezone=False))
    notes = Column(Text)

Base.metadata.create_all(engine)