from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,declarative_base

Base = declarative_base

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)

    patients = relationship("Patient",back_populates="doctor")

    def __repr__(self):
        return f"Doctor(id = {self.id}, name = '{self.name}', email = '{self.email}')"
    
class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)

    doctor = relationship("Doctor",back_populates="patients")

    def __repr__(self):
        return f"Doctor(id = {self.id}, name = '{self.name}', email = '{self.email}')"
    
class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))