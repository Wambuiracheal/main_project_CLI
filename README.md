# **DOCTOR-PATIENT CLI APP**

## **Project Description**  
This CLI-based application manages the interactions between doctors and patients, allowing users to create, update, delete, and view records for doctors, patients, and their appointments.  

### **Models and Relationships**  
1. **Doctor**  
   - A doctor can have many patients.  
   - A doctor can create multiple appointments for a patient.

2. **Patient**  
   - A patient can have many appointments.

3. **Appointment**  
   - Links a doctor and a patient.  

---

### **Features for the User**  
1. **Patient Management**  
   - Create a patient.  
   - Update a patient.  
   - Delete a patient.  
   - View all patients.  
   - View all patients associated with a specific doctor.

2. **Doctor Management**  
   - Create a doctor.  
   - Update a doctor.  
   - Delete a doctor.  
   - View all doctors.

3. **Appointment Management**  
   - View all appointments for a patient.  
   - Create an appointment for a patient.

4. **Exit the Application**  

---

## **Steps to Set Up the Project**  

1. **Install Dependencies**  
   Use `pipenv` to manage dependencies:  
   ```bash
   pipenv install sqlalchemy alembic
   ```

2. **Set Up Alembic for Database Migrations**  
   - Initialize Alembic for migrations:  
     ```bash
     alembic init migrations
     ```  

   - Modify the `alembic.ini` file:  
     Update the `sqlalchemy.url` parameter to point to your database.  

   - Update the `env.py` file inside the `migrations` folder:  
     Import the `Base` model from your SQLAlchemy setup.  

3. **Generate and Apply Migrations**  
   - Create a migration file:  
     ```bash
     alembic revision --autogenerate -m "Initial migration"
     ```  
   - Apply the migration to update the database schema:  
     ```bash
     alembic upgrade head
     ```  

4. **Run the CLI App**  
   Launch the application and interact with the features described above.  

