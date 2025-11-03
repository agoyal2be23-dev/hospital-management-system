# Hospital Management System

A comprehensive hospital management system built with Python Flask, React, and SQLite.

## Features

### Backend (Flask API)
- **Patient Management**: Create, read, update, delete patient records
- **Doctor Management**: Manage doctor profiles and specializations
- **Appointment Scheduling**: Book and manage appointments
- **Medical Records**: Store and retrieve patient medical history
- **Search Functionality**: Search across patients, doctors, and medical records
- **RESTful API**: Clean, consistent API endpoints

### Frontend (Dashboard)
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Dashboard**: Overview of system statistics
- **Patient Portal**: Comprehensive patient management interface
- **Doctor Portal**: Doctor profile and appointment management
- **Appointment System**: Easy appointment booking and status tracking
- **Medical Records**: Detailed medical history tracking

## Tech Stack

### Backend
- **Python Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **SQLite**: Database
- **Flask-Marshmallow**: Object serialization
- **Flask-CORS**: Cross-origin resource sharing
- **Gunicorn**: WSGI HTTP Server

### Frontend
- **React 18**: Frontend framework
- **Material-UI (MUI)**: UI component library
- **React Router**: Navigation
- **React Query**: Data fetching and caching
- **React Hook Form**: Form management
- **Axios**: HTTP client
- **React Toastify**: Notifications

## Project Structure

```
hospital-management-system/
├── flask_backend/
│   ├── models.py
│   ├── routes.py
│   ├── app.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── runtime.txt
│   └── .env
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
└── README.md
```

## Quick Start

### Prerequisites
- Python 3.11+ 
- Node.js (v14 or higher)
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd hospital-management-system
   ```

2. **Install Backend Dependencies (Python)**
   ```bash
   cd flask_backend
   pip install -r requirements.txt
   ```

3. **Install Frontend Dependencies**
   ```bash
   cd ../frontend
   npm install
   ```

### Development

1. **Start Flask Backend Server**
   ```bash
   cd flask_backend
   python app.py
   ```
   Server will run on http://localhost:5000

2. **Start Frontend Development Server**
   ```bash
   cd frontend
   npm start
   ```
   Frontend will run on http://localhost:3000

### Production Build

1. **Build Frontend**
   ```bash
   cd frontend
   npm run build
   ```

2. **Start Production Server**
   ```bash
   cd backend
   npm start
   ```

## API Endpoints

### Patients
- `GET /api/patients` - Get all patients
- `GET /api/patients/:id` - Get patient by ID
- `GET /api/patients/search?q=term` - Search patients
- `POST /api/patients` - Create new patient
- `PUT /api/patients/:id` - Update patient
- `DELETE /api/patients/:id` - Delete patient

### Doctors
- `GET /api/doctors` - Get all doctors
- `GET /api/doctors/:id` - Get doctor by ID
- `GET /api/doctors/search?q=term` - Search doctors
- `GET /api/doctors/specialization/:spec` - Get doctors by specialization
- `POST /api/doctors` - Create new doctor
- `PUT /api/doctors/:id` - Update doctor
- `DELETE /api/doctors/:id` - Delete doctor

### Appointments
- `GET /api/appointments` - Get all appointments
- `GET /api/appointments/:id` - Get appointment by ID
- `GET /api/appointments/patient/:patientId` - Get patient appointments
- `GET /api/appointments/doctor/:doctorId` - Get doctor appointments
- `GET /api/appointments/date/:date` - Get appointments by date
- `POST /api/appointments` - Create new appointment
- `PUT /api/appointments/:id` - Update appointment
- `PATCH /api/appointments/:id/status` - Update appointment status
- `DELETE /api/appointments/:id` - Delete appointment

### Medical Records
- `GET /api/medical-records` - Get all medical records
- `GET /api/medical-records/:id` - Get medical record by ID
- `GET /api/medical-records/search?q=term` - Search medical records
- `GET /api/medical-records/patient/:patientId` - Get patient records
- `GET /api/medical-records/doctor/:doctorId` - Get doctor records
- `POST /api/medical-records` - Create new medical record
- `PUT /api/medical-records/:id` - Update medical record
- `DELETE /api/medical-records/:id` - Delete medical record

### Health Check
- `GET /api/health` - API health check

## Database Schema

### Patients Table
- id, firstName, lastName, email, phone, dateOfBirth, gender
- address, emergencyContact, emergencyPhone
- medicalHistory, allergies, bloodType
- createdAt, updatedAt

### Doctors Table
- id, firstName, lastName, email, phone, specialization
- licenseNumber, department, experience, qualifications
- consultationFee, availability
- createdAt, updatedAt

### Appointments Table
- id, patientId, doctorId, appointmentDate, appointmentTime
- duration, status, reason, notes
- createdAt, updatedAt

### Medical Records Table
- id, patientId, doctorId, appointmentId (optional)
- diagnosis, symptoms, treatment, medications
- followUpDate, notes, recordDate
- createdAt, updatedAt

## Environment Variables

### Backend (.env)
```
PORT=5000
NODE_ENV=development
JWT_SECRET=your_jwt_secret_key_here
DB_PATH=./database.sqlite
```

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:5000/api
```

## Deployment

### Local Production
1. Build frontend: `cd frontend && npm run build`
2. Start backend: `cd backend && npm start`
3. Access at http://localhost:5000

### Heroku Deployment
1. Create Heroku app
2. Set environment variables
3. Deploy with git: `git push heroku main`

### Docker Deployment
```dockerfile
# Example Dockerfile for backend
FROM node:16-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .
EXPOSE 5000
CMD ["npm", "start"]
```

## Features in Detail

### Dashboard
- System statistics overview
- Recent appointments
- Quick access to all modules

### Patient Management
- Complete patient registration
- Medical history tracking
- Emergency contact information
- Search and filter capabilities

### Doctor Management
- Doctor profiles with specializations
- Availability management
- Experience and qualification tracking

### Appointment System
- Easy appointment booking
- Status tracking (scheduled, confirmed, completed, etc.)
- Calendar integration ready
- Conflict detection

### Medical Records
- Comprehensive medical history
- Diagnosis and treatment tracking
- Medication management
- Follow-up scheduling

## Security Features
- Input validation
- SQL injection prevention
- CORS configuration
- Environment variable protection

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License.

## Support
For support, email your-email@domain.com or create an issue in the repository.

## Roadmap
- [ ] User authentication and authorization
- [ ] Role-based access control
- [ ] Email notifications
- [ ] SMS reminders
- [ ] File upload for medical documents
- [ ] Integration with laboratory systems
- [ ] Billing and insurance management
- [ ] Telemedicine features
- [ ] Mobile app development
- [ ] Advanced reporting and analytics