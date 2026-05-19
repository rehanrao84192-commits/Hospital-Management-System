from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# ---------------- DATABASE ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rehanrao1122.",
    database="hospital_db"
)
cursor = conn.cursor()

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- ADD PATIENT ----------------
@app.route("/add_patient", methods=["POST"])
def add_patient():
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    contact = request.form["contact"]
    address = request.form["address"]

    cursor.execute("""
        INSERT INTO Patients(Name, Age, Gender, Contact, Address)
        VALUES(%s,%s,%s,%s,%s)
    """, (name, age, gender, contact, address))

    conn.commit()
    return redirect("/patients")

# ---------------- VIEW PATIENTS ----------------
@app.route("/patients")
def patients():
    cursor.execute("SELECT * FROM Patients")
    data = cursor.fetchall()
    return render_template("patients.html", patients=data)

# ---------------- VIEW DOCTORS ----------------
@app.route("/doctors")
def doctors():
    cursor.execute("SELECT * FROM Doctors")
    data = cursor.fetchall()
    return render_template("doctors.html", doctors=data)

# ---------------- ADD APPOINTMENT ----------------
@app.route("/add_appointment", methods=["POST"])
def add_appointment():
    patient = request.form["patient"]
    doctor = request.form["doctor"]
    date = request.form["date"]
    time = request.form["time"]

    cursor.execute("""
        INSERT INTO Appointments(PatientName, DoctorName, AppointmentDate, AppointmentTime)
        VALUES(%s,%s,%s,%s)
    """, (patient, doctor, date, time))

    conn.commit()
    return redirect("/appointments")

# ---------------- VIEW APPOINTMENTS ----------------
@app.route("/appointments")
def appointments():
    cursor.execute("SELECT * FROM Appointments")
    data = cursor.fetchall()
    return render_template("appointments.html", appointments=data)

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)