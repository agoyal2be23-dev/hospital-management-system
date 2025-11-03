from flask_backend.app_integrated import app, db, Patient, Doctor

def check_data():
    with app.app_context():
        patients = Patient.query.all()
        doctors = Doctor.query.all()
        
        print(f"📊 Patients in database: {len(patients)}")
        for patient in patients[:3]:
            print(f"   - Patient #{patient.id}: {patient.firstName} {patient.lastName}")
            
        print(f"\n👨‍⚕️ Doctors in database: {len(doctors)}")
        for doctor in doctors[:3]:
            print(f"   - Doctor #{doctor.id}: Dr. {doctor.firstName} {doctor.lastName} ({doctor.specialization})")

if __name__ == '__main__':
    check_data()