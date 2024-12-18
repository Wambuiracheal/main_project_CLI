from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Text
from sqlalchemy.orm import relationship,declarative_base

Base = declarative_base()

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)

    patients = relationship("Patient",back_populates="doctor", cascade="all, delete-orphan")
    appointments = relationship("Appointment",back_populates="doctor", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Doctor(id = {self.id}, name = '{self.name}', email = '{self.email}')"
    
class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    age = Column(Integer,nullable=False)
    doctor_id = Column(Integer,ForeignKey("doctors.id"), nullable=False)

    doctor = relationship("Doctor",back_populates="patients")
    appointments = relationship("Appointment",back_populates="patient", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Doctor(id = {self.id}, name = '{self.name}', email = '{self.email}', doctor_id={self.doctor_id})"
    
class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    details = Column(Text)

    doctor = relationship("Doctor",back_populates="appointments")
    patient = relationship("Patient",back_populates="appointments")

    def __repr__(self):
        return (
            f"Appointment(id={self.id}, doctor_id={self.doctor_id}, "
            f"patient_id={self.patient_id}, appointment_date={self.appointment_date}, details='{self.details}')"
        )