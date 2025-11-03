#!/bin/bash

echo "🏥 Hospital Management System - Flask Setup"
echo "=========================================="

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.11+ first."
    exit 1
fi

# Check Python version
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "✅ Python version: $python_version"

# Navigate to flask_backend directory
cd flask_backend

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Backend dependencies installed successfully!"
else
    echo "❌ Failed to install backend dependencies"
    exit 1
fi

# Navigate to frontend directory
cd ../frontend

echo "📦 Installing Node.js dependencies..."
npm install

if [ $? -eq 0 ]; then
    echo "✅ Frontend dependencies installed successfully!"
else
    echo "❌ Failed to install frontend dependencies"
    exit 1
fi

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "To start the application:"
echo "1. Backend:  cd flask_backend && python app.py"
echo "2. Frontend: cd frontend && npm start"
echo ""
echo "Access your application at:"
echo "- Frontend: http://localhost:3000"
echo "- Backend API: http://localhost:5000/api"