import sys
from datetime import datetime
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
    name = input("Enter Doctor name: ")
    email = input("Enter Doctor Email: ")
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


# PATIENT CRUD OPERATION

def create_patient():
    name = input("Enter patient's name: ")
    email = input("Enter patient's email: ")
    age = int(input("Enter patient's age: "))
    doctor_id = int(input("Enter doctor ID: "))
    doctor = session.get(Doctor,doctor_id)
    
    if not doctor:
        print(f"Doctor with ID {doctor_id} does not exist.")
        return
    patient = Patient(name=name, email=email, age=age, doctor_id=doctor_id)
    session.add(patient)
    session.commit()
    print(f"Patient '{name}' created with ID {patient.id} and assigned to Doctor with ID {doctor_id} and name '{doctor.name}'")
    

def update_patient():
    patient_id = int(input("Enter Patient ID to update: "))
    patient = session.get(Patient,patient_id)
    if not patient:
        print(f"Patient with ID {patient_id} can not be found!!!")
        return
    patient.name = input(f"Update patient's name: (current: {patient.name}): ") or patient.name
    patient.email = input(f"Update patient's email: (current: {patient.email}): ") or patient.email
    patient.age = input(f"Update patient's age: (current: {patient.age}: )") or patient.age
    new_doctor_id = input(f"Update new doctor's ID: (current: {patient.doctor_id}: )") or patient.doctor_id
    if new_doctor_id:
        new_doctor_id = session.get(Doctor,int(new_doctor_id))
        if not new_doctor_id:
            print(f"Doctor with {new_doctor_id} cannot be found. Onto the next...")
        else:
            patient.doctor_id = new_doctor_id
    session.commit()
    print(f"Patient ID: {patient_id} has been updated successfully!!!")

def delete_patient():
    patient_id = int(input("Enter patient ID to delete: "))
    patient = session.get(Patient,patient_id)

    if not patient:
        print(f"patient with ID {patient_id} cannot be found!!!")
        return
    session.delete(patient)
    session.commit()
    print(f"patient ID {patient_id} deleted successfully.")

def assign_patient():
    patient_id = int(input("Enter Patient ID: "))
    doctor_id = int(input("Enter the new Doctor ID: "))
    patient = session.get(Patient,patient_id)
    doctor = session.get(Doctor,doctor_id)

    if not patient or not doctor:
        print("Invalid patient ID  or doctor ID")
        return
    patient.doctor_id = doctor_id
    session.commit()
    print("Doctor assigned successfully")

# APPOINTMENTS
def create_appointment():
    list_doctors()
    doctor_id = int(input("Enter Patient ID to create an appointment: "))
    doctor = session.get(Doctor, doctor_id)
    if not doctor:
        print(f"No doctor found with ID {doctor_id}.")
        return
    
    list_patients()
    patient_id = int(input("Enter Patient ID to create an appointment: "))
    patient = session.get(Patient, patient_id)
    if not patient:
        print(f"No patient found with ID {patient_id}.")
        return
    
    appointment_date = input("Enter appointment date (YYYY-MM-DD HH:MM): ")
    try:
        appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date format.")
        return

    details = input("Enter appointment details: ")

    new_appointment = Appointment(
        doctor_id=doctor_id,
        patient_id=patient_id,
        appointment_date=appointment_date,
        details=details,
    )
    session.add(new_appointment)
    session.commit()
    print(f"Appointment created successfully for Patient {patient.name} with Doctor {doctor.name}.")

def update_appointment():
    list_appointments()
    appointment_id = int(input("Enter Appointment ID to update: "))
    appointment = session.get(Appointment, appointment_id)
    if not appointment:
        print(f"No appointment found with ID {appointment_id}.")
        return

    new_date = input(f"Update appointment date (current: {appointment.appointment_date}, format: YYYY-MM-DD HH:MM): ")
    if new_date:
        try:
            appointment.appointment_date = datetime.strptime(new_date, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format. Appointment date not updated.")

    appointment.details = input(f"Update appointment details (current: {appointment.details}): ") or appointment.details
    session.commit()
    print(f"Appointment ID {appointment_id} has been updated successfully.")

def delete_appointment():
    list_appointments()
    appointment_id = int(input("Enter Appointment ID to delete: "))
    appointment = session.get(Appointment, appointment_id)
    if not appointment:
        print(f"No appointment found with ID {appointment_id}.")
        return

    session.delete(appointment)
    session.commit()
    print(f"Appointment ID {appointment_id} deleted successfully.")

def list_appointments():
    appointments = session.query(Appointment).all()
    if not appointments:
        print("No appointments found.")
        return
    for appt in appointments:
        doctor = session.get(Doctor, appt.doctor_id)
        patient = session.get(Patient, appt.patient_id)
        print(
            f"ID: {appt.id}, Doctor: {doctor.name}, Patient: {patient.name}, "
            f"Date: {appt.appointment_date}, Details: {appt.details}"
        )

def list_doctors():
    doctors = session.query(Doctor).all()
    if not doctors:
        print('No doctors found!!!')
    for doctor in doctors:
        print(doctor)

def list_patients():
    patients = session.query(Patient).all()
    if not patients:
        print('No doctors found!!1')
    for patient in patients:
        print(patient)

def view_patients_by_doctor():
    doctor_id = int(input("Enter Doctor ID to view patients: "))
    doctor = session.get(Doctor,doctor_id)
    if not doctor:
        print(f"Doctor with ID {doctor_id} does not exist")
        return
    patients = doctor.patients
    if not patients:
        print(f"No patients found under the doctor with ID {doctor_id}")
        return
    print(f"Patients belonging to Doctor '{doctor.name}' (ID {doctor_id}): ")
    for patient in patients:
        print(patient)

def main_menu():
    while True:
        print("\nWelcome to our doctor patient database, what do you have in mind🤔?")
        print("1. Create Doctor")
        print("2. Update Doctor")
        print("3. Delete Doctor")
        print("4. Create Patient")
        print("5. Update Patient")
        print("6. Delete Patient")
        print("7. Assign a patient to a doctor")
        print("8. List Doctors")
        print("9. List Patients")
        print("10.View Patients by Doctor")
        print("11.Create Appointment")
        print("12.Update Appointment")
        print("13.Delete Appointment")
        print("14.List Appointments")
        print("15. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_doctor()
        elif choice == "2":
            update_doctor()
        elif choice == "3":
            delete_doctor()
        elif choice == "4":
            create_patient()
        elif choice == "5":
            update_patient()
        elif choice == "6":
            delete_patient()
        elif choice == "7":
            assign_patient()
        elif choice == "8":
            list_doctors()
        elif choice == "9":
            list_patients()
        elif choice == "10":
            view_patients_by_doctor()
        elif choice =="11":
            create_appointment()
        elif choice == "12"
            update

        elif choice == "15":
            exit()



if __name__== "__main__":
    init_db()
    main_menu()
    

