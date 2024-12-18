import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Doctor,Patient,Appointment

DATABASE_URL = "sqlite:///patients.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
    print("Successful initialization of the database")

# DOCTOR CRUD OPERATION

def create_doctor():
    name = input("Enter Patient name: ")
    email = input("Enter Patient Email: ")
    doctor = Doctor(name=name,email=email)
    session.add(doctor)
    session.commit()
    print(f"Doctor '{name}' created with ID {doctor.id}")

def update_doctor():
    doctor_id = int(input("Enter Doctor ID to update: "))
    doctor = session.get(Doctor,doctor_id)
    if not doctor:
        print(f"Doctor with ID {doctor_id} can not be found!!!")
        return
    doctor.name = input(f"Update doctor's name: (current: {doctor.name}): ") or doctor.name
    doctor.email = input(f"Update doctor's email: (current: {doctor.email}): ") or doctor.email
    session.commit()
    print(f"Doctor ID: {doctor_id} has been updated successfully!!!")

def delete_doctor():
    doctor_id = int(input("Enter the doctor's ID to delete: "))
    doctor = session.get(Doctor,doctor_id)

    if not doctor:
        print(f"Doctor with ID {doctor_id} does not exist.")
        return
    session.delete(doctor)
    session.commit()
    print(f"Doctor ID {doctor_id} deleted successfully.")


if __name__== "__main__":
    init_db()
    

