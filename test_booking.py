import requests
import json
from datetime import datetime, timedelta

def test_appointment_booking():
    base_url = "http://127.0.0.1:5000"
    
    # Test data for appointment booking
    test_appointment = {
        "patient_id": 1,  # Assuming patient with ID 1 exists
        "doctor_id": 6,   # Dr. Sarah Wilson (Breast Cancer Oncology)
        "appointmentDate": (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'),
        "appointmentTime": "10:00",
        "type": "Consultation",
        "reason": "Breast cancer screening consultation",
        "duration": 30,
        "fees": 250.00
    }
    
    print("🧪 Testing Appointment Booking API...")
    print(f"📅 Booking appointment for: {test_appointment['appointmentDate']} at {test_appointment['appointmentTime']}")
    
    try:
        response = requests.post(
            f"{base_url}/api/appointments",
            headers={'Content-Type': 'application/json'},
            json=test_appointment
        )
        
        print(f"📊 Response Status: {response.status_code}")
        
        if response.status_code == 201:
            result = response.json()
            print("✅ Appointment booked successfully!")
            print(f"📋 Appointment Details:")
            print(f"   - ID: {result['data']['id']}")
            print(f"   - Patient ID: {result['data']['patient_id']}")
            print(f"   - Doctor ID: {result['data']['doctor_id']}")
            print(f"   - Date: {result['data']['appointmentDate']}")
            print(f"   - Time: {result['data']['appointmentTime']}")
            print(f"   - Type: {result['data']['type']}")
            print(f"   - Fees: ${result['data']['fees']}")
            
        else:
            print("❌ Failed to book appointment")
            try:
                error_data = response.json()
                print(f"   Error: {error_data.get('message', 'Unknown error')}")
            except:
                print(f"   Raw response: {response.text}")
                
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed - Make sure Flask server is running on http://127.0.0.1:5000")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    # Test getting all appointments
    print(f"\n📋 Testing Get All Appointments...")
    try:
        response = requests.get(f"{base_url}/api/appointments")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Found {result['count']} appointments")
            for apt in result['data'][:3]:  # Show first 3
                print(f"   - Appointment #{apt['id']}: Patient {apt['patient_id']} with Doctor {apt['doctor_id']} on {apt['appointmentDate']}")
        else:
            print(f"❌ Failed to get appointments: {response.status_code}")
    except Exception as e:
        print(f"❌ Error getting appointments: {e}")

if __name__ == '__main__':
    test_appointment_booking()