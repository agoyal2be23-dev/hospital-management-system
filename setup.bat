@echo off
echo 🏥 Hospital Management System - Flask Setup
echo ==========================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.11+ first.
    pause
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set python_version=%%i
echo ✅ Python version: %python_version%

REM Navigate to flask_backend directory
cd flask_backend

echo 📦 Installing Python dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Failed to install backend dependencies
    pause
    exit /b 1
)

echo ✅ Backend dependencies installed successfully!

REM Navigate to frontend directory
cd ..\frontend

echo 📦 Installing Node.js dependencies...
npm install

if %errorlevel% neq 0 (
    echo ❌ Failed to install frontend dependencies
    pause
    exit /b 1
)

echo ✅ Frontend dependencies installed successfully!

echo.
echo 🎉 Setup completed successfully!
echo.
echo To start the application:
echo 1. Backend:  cd flask_backend ^&^& python app.py
echo 2. Frontend: cd frontend ^&^& npm start
echo.
echo Access your application at:
echo - Frontend: http://localhost:3000
echo - Backend API: http://localhost:5000/api

pause