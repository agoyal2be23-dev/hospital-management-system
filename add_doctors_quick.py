import requests
import json

# API endpoint for adding more doctors (if we had one)
# For now, we'll add doctors via direct database access

from flask_backend.app_integrated import app, db, Doctor
from datetime import datetime

def add_doctors_via_database():
    with app.app_context():
        doctors_to_add = [
            {
                'firstName': 'Amanda',
                'lastName': 'Foster',
                'email': 'dr.amanda.foster@hospital.com',
                'phone': '+1-555-0119',
                'specialization': 'Cardiology',
                'qualification': 'MD, FACC - Interventional Cardiology',
                'experience': 12,
                'consultationFee': 180.00,
                'bio': 'Leading cardiologist specializing in interventional procedures and heart disease prevention.',
                'status': 'active',
                'availability': {
                    'monday': '9:00 AM - 5:00 PM',
                    'tuesday': '9:00 AM - 5:00 PM',
                    'wednesday': '9:00 AM - 3:00 PM',
                    'thursday': '9:00 AM - 5:00 PM',
                    'friday': '9:00 AM - 4:00 PM',
                    'saturday': '10:00 AM - 2:00 PM',
                    'sunday': 'Closed'
                }
            },
            {
                'firstName': 'James',
                'lastName': 'Mitchell',
                'email': 'dr.james.mitchell@hospital.com',
                'phone': '+1-555-0120',
                'specialization': 'Orthopedic Surgery',
                'qualification': 'MD, MS Orthopedics - Joint Replacement',
                'experience': 15,
                'consultationFee': 200.00,
                'bio': 'Expert orthopedic surgeon with focus on joint replacement and sports medicine.',
                'status': 'active',
                'availability': {
                    'monday': '8:00 AM - 6:00 PM',
                    'tuesday': '8:00 AM - 6:00 PM',
                    'wednesday': '8:00 AM - 4:00 PM',
                    'thursday': '8:00 AM - 6:00 PM',
                    'friday': '8:00 AM - 4:00 PM',
                    'saturday': '9:00 AM - 1:00 PM',
                    'sunday': 'Closed'
                }
            },
            {
                'firstName': 'Lisa',
                'lastName': 'Wang',
                'email': 'dr.lisa.wang@hospital.com',
                'phone': '+1-555-0121',
                'specialization': 'Dermatology',
                'qualification': 'MD, Dermatology - Cosmetic & Medical',
                'experience': 8,
                'consultationFee': 160.00,
                'bio': 'Board-certified dermatologist providing comprehensive skin care and cosmetic treatments.',
                'status': 'active',
                'availability': {
                    'monday': '10:00 AM - 6:00 PM',
                    'tuesday': '10:00 AM - 6:00 PM',
                    'wednesday': '10:00 AM - 4:00 PM',
                    'thursday': '10:00 AM - 6:00 PM',
                    'friday': '10:00 AM - 5:00 PM',
                    'saturday': '10:00 AM - 3:00 PM',
                    'sunday': 'Closed'
                }
            },
            {
                'firstName': 'Carlos',
                'lastName': 'Hernandez',
                'email': 'dr.carlos.hernandez@hospital.com',
                'phone': '+1-555-0122',
                'specialization': 'Neurology',
                'qualification': 'MD, PhD Neuroscience - Movement Disorders',
                'experience': 18,
                'consultationFee': 220.00,
                'bio': 'Neurologist specializing in movement disorders, epilepsy, and neurodegenerative diseases.',
                'status': 'active',
                'availability': {
                    'monday': '9:00 AM - 5:00 PM',
                    'tuesday': '9:00 AM - 5:00 PM',
                    'wednesday': '9:00 AM - 3:00 PM',
                    'thursday': '9:00 AM - 5:00 PM',
                    'friday': '9:00 AM - 4:00 PM',
                    'saturday': 'Closed',
                    'sunday': 'Closed'
                }
            },
            {
                'firstName': 'Rachel',
                'lastName': 'Singh',
                'email': 'dr.rachel.singh@hospital.com',
                'phone': '+1-555-0123',
                'specialization': 'Pediatrics',
                'qualification': 'MD, Pediatrics - Child Development',
                'experience': 10,
                'consultationFee': 140.00,
                'bio': 'Pediatrician dedicated to comprehensive child healthcare and developmental medicine.',
                'status': 'active',
                'availability': {
                    'monday': '8:00 AM - 5:00 PM',
                    'tuesday': '8:00 AM - 5:00 PM',
                    'wednesday': '8:00 AM - 3:00 PM',
                    'thursday': '8:00 AM - 5:00 PM',
                    'friday': '8:00 AM - 3:00 PM',
                    'saturday': '9:00 AM - 1:00 PM',
                    'sunday': 'Closed'
                }
            }
        ]
        
        added_count = 0
        for doctor_data in doctors_to_add:
            # Check if doctor already exists
            existing_doctor = Doctor.query.filter_by(email=doctor_data['email']).first()
            if not existing_doctor:
                doctor = Doctor(**doctor_data)
                db.session.add(doctor)
                added_count += 1
        
        try:
            db.session.commit()
            print(f"✅ Successfully added {added_count} new doctors to the database")
            
            # Show all doctors
            all_doctors = Doctor.query.all()
            print(f"\n📊 Total doctors in database: {len(all_doctors)}")
            
            print("\n👨‍⚕️ All Doctors:")
            for doc in all_doctors:
                print(f"   • Dr. {doc.firstName} {doc.lastName} ({doc.specialization})")
                
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error adding doctors: {e}")

if __name__ == '__main__':
    add_doctors_via_database()