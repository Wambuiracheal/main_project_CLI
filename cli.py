import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Doctor,Patient,Appointment

DATABASE_URL = "sqlite:///patients.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()



