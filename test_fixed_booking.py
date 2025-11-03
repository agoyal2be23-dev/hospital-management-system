import requests
import json

def test_appointment_with_correct_format():
    url = "http://127.0.0.1:5000/api/appointments"
    
    # Test data with correct format
    appointment_data = {
        "patient_id": 1,
        "doctor_id": 6,  # Dr. Sarah Wilson (Breast Cancer Oncology)
        "appointmentDate": "2025-09-16",  # Tomorrow
        "appointmentTime": "10:30",       # 10:30 AM
        "type": "Consultation",
        "reason": "Breast cancer consultation and screening",
        "duration": 60
    }
    
    print("🧪 Testing Appointment Booking with correct format...")
    print(f"📋 Data being sent: {json.dumps(appointment_data, indent=2)}")
    
    try:
        response = requests.post(
            url,
            headers={'Content-Type': 'application/json'},
            json=appointment_data
        )
        
        print(f"📊 Response Status: {response.status_code}")
        print(f"📄 Response: {response.text}")
        
        if response.status_code == 201:
            result = response.json()
            print("✅ Appointment booked successfully!")
            print(f"   - Appointment ID: {result['data']['id']}")
        else:
            print("❌ Failed to book appointment")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed - Make sure Flask server is running")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_patient_creation():
    url = "http://127.0.0.1:5000/api/patients"
    
    # Test patient data
    patient_data = {
        "firstName": "Test",
        "lastName": "Patient",
        "email": "test.patient@email.com",
        "phone": "+1-555-9999",
        "dateOfBirth": "1990-05-15",
        "gender": "Female",
        "address": "123 Test Street, Test City",
        "emergencyContact": "Test Emergency Contact",
        "emergencyPhone": "+1-555-8888",
        "bloodType": "A+",
        "allergies": "None",
        "medicalHistory": "No major issues"
    }
    
    print("\n🧪 Testing Patient Creation...")
    print(f"📋 Data being sent: {json.dumps(patient_data, indent=2)}")
    
    try:
        response = requests.post(
            url,
            headers={'Content-Type': 'application/json'},
            json=patient_data
        )
        
        print(f"📊 Response Status: {response.status_code}")
        print(f"📄 Response: {response.text}")
        
        if response.status_code == 201:
            result = response.json()
            print("✅ Patient created successfully!")
            print(f"   - Patient ID: {result['data']['id']}")
        else:
            print("❌ Failed to create patient")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed - Make sure Flask server is running")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    test_patient_creation()
    test_appointment_with_correct_format()