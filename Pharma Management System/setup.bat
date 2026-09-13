@echo off
echo ========================================
echo  MediCare Pharmacy Management System
echo ========================================
echo.
echo Installing required packages...
pip install -r requirements.txt
echo.
echo ========================================
echo Starting the application...
echo Open your browser and go to: http://localhost:5001
echo Admin Login: username=admin, password=admin123
echo Press Ctrl+C to stop the server
echo ========================================
echo.
python app.py
pause