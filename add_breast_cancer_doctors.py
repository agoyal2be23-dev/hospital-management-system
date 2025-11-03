from flask_backend.app_integrated import app, db, Doctor
from datetime import datetime

def add_breast_cancer_specialists():
    with app.app_context():
        # Breast Cancer Specialists
        breast_cancer_doctors = [
            {
                'firstName': 'Sarah',
                'lastName': 'Wilson',
                'email': 'dr.sarah.wilson@hospital.com',
                'phone': '+1-555-0101',
                'specialization': 'Breast Cancer Oncology',
                'qualification': 'MD, Medical Oncology - Breast Cancer Fellowship',
                'experience': 15,
                'consultationFee': 250.00,
                'bio': 'Leading breast cancer oncologist with expertise in precision medicine, immunotherapy, and clinical trials for advanced breast cancer.',
                'status': 'active',
                'availability': {
                    'monday': '9:00 AM - 5:00 PM',
                    'tuesday': '9:00 AM - 5:00 PM',
                    'wednesday': '9:00 AM - 3:00 PM',
                    'thursday': '9:00 AM - 5:00 PM',
                    'friday': '9:00 AM - 4:00 PM',
                    'saturday': '9:00 AM - 1:00 PM',
                    'sunday': 'Closed'
                }
            },
            {
                'firstName': 'Michael',
                'lastName': 'Chen',
                'email': 'dr.michael.chen@hospital.com',
                'phone': '+1-555-0102',
                'specialization': 'Breast Surgical Oncology',
                'qualification': 'MD, Surgical Oncology - Breast Surgery Fellowship',
                'experience': 12,
                'consultationFee': 280.00,
                'bio': 'Expert breast surgical oncologist specializing in minimally invasive techniques, oncoplastic surgery, and lymph node procedures.',
                'status': 'active',
                'availability': {
                    'monday': '8:00 AM - 6:00 PM',
                    'tuesday': '8:00 AM - 6:00 PM',
                    'wednesday': '8:00 AM - 4:00 PM',
                    'thursday': '8:00 AM - 6:00 PM',
                    'friday': '8:00 AM - 4:00 PM',
                    'saturday': '9:00 AM - 2:00 PM',
                    'sunday': 'Closed'
                }
            },
            {
                'firstName': 'Emily',
                'lastName': 'Rodriguez',
                'email': 'dr.emily.rodriguez@hospital.com',
                'phone': '+1-555-0103',
                'specialization': 'Medical Oncology - Breast Cancer',
                'qualification': 'MD, PhD, Medical Oncology - Breast Cancer Specialist',
                'experience': 18,
                'consultationFee': 240.00,
                'bio': 'Medical oncologist focused on breast cancer chemotherapy, targeted therapy, hormone therapy, and survivorship care.',
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
                'firstName': 'David',
                'lastName': 'Thompson',
                'email': 'dr.david.thompson@hospital.com',
                'phone': '+1-555-0104',
                'specialization': 'Radiation Oncology - Breast Cancer',
                'qualification': 'MD, Radiation Oncology - Breast Cancer Fellowship',
                'experience': 14,
                'consultationFee': 220.00,
                'bio': 'Radiation oncologist expert in breast cancer radiation therapy, IMRT, stereotactic radiation, and brachytherapy.',
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
            },
            {
                'firstName': 'Jennifer',
                'lastName': 'Kumar',
                'email': 'dr.jennifer.kumar@hospital.com',
                'phone': '+1-555-0105',
                'specialization': 'Breast Cancer Genetics & Prevention',
                'qualification': 'MD, MS Genetic Counseling - Cancer Genetics',
                'experience': 10,
                'consultationFee': 200.00,
                'bio': 'Cancer geneticist specializing in BRCA testing, hereditary breast cancer syndromes, and prevention strategies.',
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
                'firstName': 'Robert',
                'lastName': 'Kim',
                'email': 'dr.robert.kim@hospital.com',
                'phone': '+1-555-0106',
                'specialization': 'Plastic & Reconstructive Surgery - Breast',
                'qualification': 'MD, Plastic Surgery - Breast Reconstruction Fellowship',
                'experience': 16,
                'consultationFee': 300.00,
                'bio': 'Plastic surgeon expert in breast reconstruction, microsurgical techniques, and aesthetic breast surgery.',
                'status': 'active',
                'availability': {
                    'monday': '8:00 AM - 6:00 PM',
                    'tuesday': '8:00 AM - 6:00 PM',
                    'wednesday': '8:00 AM - 4:00 PM',
                    'thursday': '8:00 AM - 6:00 PM',
                    'friday': '8:00 AM - 4:00 PM',
                    'saturday': '9:00 AM - 3:00 PM',
                    'sunday': 'Closed'
                }
            }
        ]
        
        added_count = 0
        for doctor_data in breast_cancer_doctors:
            # Check if doctor already exists
            existing_doctor = Doctor.query.filter_by(email=doctor_data['email']).first()
            if not existing_doctor:
                doctor = Doctor(**doctor_data)
                db.session.add(doctor)
                added_count += 1
        
        try:
            db.session.commit()
            print(f"✅ Successfully added {added_count} breast cancer specialists")
            
            # Show all doctors now
            all_doctors = Doctor.query.all()
            print(f"\n📊 Total doctors in database: {len(all_doctors)}")
            
            print("\n👨‍⚕️ All Doctors:")
            for doc in all_doctors:
                print(f"   • Dr. {doc.firstName} {doc.lastName} ({doc.specialization})")
                
            # Show breast cancer specialists
            breast_docs = Doctor.query.filter(
                Doctor.specialization.ilike('%breast%')
            ).all()
            
            print(f"\n🎗️ Breast Cancer Specialists ({len(breast_docs)}):")
            for doc in breast_docs:
                print(f"   • Dr. {doc.firstName} {doc.lastName} ({doc.specialization})")
                
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error adding doctors: {e}")

if __name__ == '__main__':
    add_breast_cancer_specialists()