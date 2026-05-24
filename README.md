# Hospital-Management-System
# Hospital Management System

## 📌 Project Description
Hospital Management System is a Python + MySQL based project that helps manage hospital operations easily.

In this project:
- Doctors can be added
- Patients can be managed
- Appointments can be booked
- Doctors list can be viewed

## 🛠 Technologies Used
- Python
- Tkinter GUI
- MySQL Database
- mysql-connector-python

## 💻 Features
- Add Doctor
- Add Patient
- Book Appointment
- View Doctors
- Database Connectivity

## 🗄 Database Setup

### Create Database
```sql
CREATE DATABASE hospital_db;
USE hospital_db;
```

### Doctors Table
```sql
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_name VARCHAR(100),
    specialization VARCHAR(100),
    contact VARCHAR(20)
);

### Patients Table
sql
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    contact VARCHAR(20)
);

### Appointments Table
sql
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100),
    doctor_name VARCHAR(100),
    appointment_date VARCHAR(50),
    appointment_time VARCHAR(50)
);

## ▶ How to Run Project

### Install Required Library
bash
pip install mysql-connector-python

### Run the Project
bash
python app.py

## 👨‍💻 Developer
Rehan Rao
