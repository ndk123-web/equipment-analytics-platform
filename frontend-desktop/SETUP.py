"""
Desktop Application Setup Guide

Quick Start:
1. Windows: Double-click run.bat
2. Linux/macOS: chmod +x run.sh && ./run.sh
3. Manual: python main.py (after installing requirements)

Setup Steps:
1. python -m venv venv
2. venv\Scripts\activate (Windows) or source venv/bin/activate (Linux/macOS)
3. pip install -r requirements.txt
4. python main.py

First Time Setup:
- Ensure backend is running on http://localhost:8000
- Use the Signup option to create a new account
- Or use existing credentials if backend has users

Features:
✓ Login & Signup with JWT authentication
✓ Upload CSV files (must have: Type, FlowRate, Pressure, Temperature columns)
✓ View upload history with pagination
✓ Automatic token refresh

File Format Example:
Type,FlowRate,Pressure,Temperature
Pump,45.2,100.5,25.3
Valve,32.1,98.2,24.8

For issues, check config.py and ensure backend endpoint is correct.
"""

if __name__ == '__main__':
    print(__doc__)
