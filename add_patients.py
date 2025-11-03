from flask_backend.app_integrated import app, db, Patient
from datetime import datetime, date

def add_sample_patients():
    with app.app_context():
        patients_data = [
            {
                'firstName': 'Emma',
                'lastName': 'Johnson',
                'email': 'emma.johnson@email.com',
                'phone': '+1-555-0201',
                'dateOfBirth': date(1985, 3, 15),
                'gender': 'Female',
                'address': '123 Main Street, New York, NY 10001',
                'emergencyContact': 'John Johnson (Husband)',
                'emergencyPhone': '+1-555-0202',
                'bloodType': 'O+',
                'allergies': 'None known',
                'medicalHistory': 'Annual checkups, no major issues'
            },
            {
                'firstName': 'Michael',
                'lastName': 'Davis',
                'email': 'michael.davis@email.com',
                'phone': '+1-555-0203',
                'dateOfBirth': date(1978, 8, 22),
                'gender': 'Male',
                'address': '456 Oak Avenue, Los Angeles, CA 90210',
                'emergencyContact': 'Linda Davis (Wife)',
                'emergencyPhone': '+1-555-0204',
                'bloodType': 'A+',
                'allergies': 'Penicillin',
                'medicalHistory': 'Hypertension, managed with medication'
            },
            {
                'firstName': 'Sarah',
                'lastName': 'Williams',
                'email': 'sarah.williams@email.com',
                'phone': '+1-555-0205',
                'dateOfBirth': date(1990, 12, 5),
                'gender': 'Female',
                'address': '789 Pine Road, Chicago, IL 60601',
                'emergencyContact': 'Robert Williams (Father)',
                'emergencyPhone': '+1-555-0206',
                'bloodType': 'B+',
                'allergies': 'Shellfish',
                'medicalHistory': 'Family history of breast cancer'
            },
            {
                'firstName': 'James',
                'lastName': 'Brown',
                'email': 'james.brown@email.com',
                'phone': '+1-555-0207',
                'dateOfBirth': date(1982, 6, 18),
                'gender': 'Male',
                'address': '321 Elm Street, Houston, TX 77001',
                'emergencyContact': 'Mary Brown (Mother)',
                'emergencyPhone': '+1-555-0208',
                'bloodType': 'AB+',
                'allergies': 'None known',
                'medicalHistory': 'Regular athlete, no major health issues'
            },
            {
                'firstName': 'Lisa',
                'lastName': 'Miller',
                'email': 'lisa.miller@email.com',
                'phone': '+1-555-0209',
                'dateOfBirth': date(1975, 11, 30),
                'gender': 'Female',
                'address': '654 Maple Drive, Phoenix, AZ 85001',
                'emergencyContact': 'David Miller (Brother)',
                'emergencyPhone': '+1-555-0210',
                'bloodType': 'O-',
                'allergies': 'Latex',
                'medicalHistory': 'Breast cancer survivor, regular monitoring'
            }
        ]
        
        added_count = 0
        for patient_data in patients_data:
            # Check if patient already exists
            existing_patient = Patient.query.filter_by(email=patient_data['email']).first()
            if not existing_patient:
                patient = Patient(**patient_data)
                db.session.add(patient)
                added_count += 1
        
        try:
            db.session.commit()
            print(f"✅ Successfully added {added_count} patients")
            
            # Show all patients
            all_patients = Patient.query.all()
            print(f"\n📊 Total patients in database: {len(all_patients)}")
            
            print("\n👤 All Patients:")
            for patient in all_patients:
                print(f"   • Patient #{patient.id}: {patient.firstName} {patient.lastName} ({patient.email})")
                
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error adding patients: {e}")

if __name__ == '__main__':
    add_sample_patients()