#!/usr/bin/env python3
"""
MediCare Pharmacy Management System
Quick Start Script

This script automatically sets up and runs the pharmacy management system.
No manual configuration required.
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("🔧 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please run manually:")
        print("   pip install -r requirements.txt")
        return False

def run_application():
    """Run the Flask application"""
    print("🚀 Starting MediCare Pharmacy Management System...")
    print("📱 Open your browser and go to: http://localhost:5001")
    print("👤 Admin Login: username=admin, password=admin123")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Thank you for using MediCare!")

def main():
    print("🏥 MediCare Pharmacy Management System")
    print("=" * 50)
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found!")
        return
    
    # Install requirements
    if install_requirements():
        print("\n" + "=" * 50)
        run_application()

if __name__ == "__main__":
    main()