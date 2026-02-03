"""
PyQt5 Desktop Application Installation & Deployment Guide
=========================================================

Prerequisites:
- Python 3.8 or higher installed on your system
- Backend server running on http://localhost:8000
- Minimum 100MB disk space
- Any modern Windows/macOS/Linux system

Quick Start (Windows):
1. Open Command Prompt or PowerShell
2. Navigate to: C:\Users\Navnath\OneDrive\Desktop\Fun\FOSSE-Internship\frontend-desktop
3. Run: run.bat
4. Application will start automatically

Quick Start (Linux/macOS):
1. Open Terminal
2. Navigate to: ~/Desktop/Fun/FOSSE-Internship/frontend-desktop
3. Run: chmod +x run.sh && ./run.sh
4. Application will start automatically

Manual Installation:
1. Open terminal/command prompt
2. Navigate to frontend-desktop folder
3. python -m venv venv
4. Activate venv:
   - Windows: venv\Scripts\activate
   - Linux/macOS: source venv/bin/activate
5. pip install -r requirements.txt
6. python main.py

Testing:
To verify installation is correct, run:
venv\Scripts\python -c "from PyQt5.QtWidgets import QApplication; print('✓ PyQt5 is working')"

Features:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. LOGIN SYSTEM
   - Username/password authentication
   - JWT token-based security
   - Automatic token refresh
   - Persistent login (session saved)

2. USER REGISTRATION
   - Create new account
   - Optional: email, first name, last name
   - Password confirmation
   - Input validation

3. DASHBOARD
   - Welcome message with username
   - Two tabs: Upload & History
   - Logout button
   - Session management

4. FILE UPLOAD
   - Browse & select CSV files
   - File validation (must be .csv)
   - Progress indication
   - Success/error feedback
   - Shows upload statistics:
     * Total records
     * Average FlowRate
     * Average Power

5. UPLOAD HISTORY
   - View all uploaded files
   - Pagination (10 items per page)
   - Display columns:
     * File Name
     * Total Rows
     * Avg FlowRate
     * Avg Power
     * Equipment Types
     * Date Uploaded
   - Previous/Next navigation

API Endpoints Used:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST   /api/app1/token/              - User login
POST   /api/signup/                  - User registration
POST   /api/desktop/upload           - File upload
GET    /api/get-history/             - View upload history
POST   /api/app1/token/refresh/      - Refresh access token

CSV File Format:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Required Columns:
- Type         (string): Equipment type name
- FlowRate     (number): Flow rate value
- Pressure     (number): Pressure value
- Temperature  (number): Temperature value

Example CSV:
Type,FlowRate,Pressure,Temperature
Pump,45.2,100.5,25.3
Valve,32.1,98.2,24.8
Motor,50.3,102.1,26.1
Compressor,38.5,105.2,26.5

Configuration:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Edit config.py to customize:

API_BASE_URL = "http://localhost:8000/api"
  → Change if backend is on different server

API_TIMEOUT = 10
  → Adjust timeout duration (seconds)

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
  → Set default window dimensions

WINDOW_TITLE = "Equipment Data Management Desktop"
  → Set application window title

TOKEN_STORAGE_FILE = "auth_tokens.json"
  → Location to store session tokens

Troubleshooting:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. "Cannot connect to backend"
   Solution: Ensure Django backend is running
   Command: python manage.py runserver

2. "Login fails with error 400"
   Solution: Check username/password or create new account

3. "File upload fails"
   Solution: Verify CSV format and columns

4. "PyQt5 import error"
   Solution: Reinstall: pip install --upgrade PyQt5

5. "Application won't start"
   Solution: Clear auth_tokens.json and try again

Building Executable (Windows):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. pip install pyinstaller
2. pyinstaller --onefile --windowed --name "EquipmentManager" main.py
3. Executable will be in dist/ folder
4. Create a shortcut on desktop for easy access

File Structure:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
frontend-desktop/
├── main.py                  # Application entry point
├── config.py                # Configuration settings
├── auth_manager.py          # Token & auth management
├── api_client.py            # API communication
├── login_screen.py          # Login UI components
├── signup_screen.py         # Signup UI components
├── dashboard_screen.py      # Dashboard UI components
├── requirements.txt         # Python dependencies
├── run.bat                  # Windows startup script
├── run.sh                   # Linux/macOS startup script
├── README.md                # User documentation
├── .gitignore              # Git ignore patterns
└── venv/                    # Virtual environment (auto-created)

Performance Tips:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Large CSV files: 100MB+ may take a few seconds
- History pagination: Loads 10 records per page efficiently
- Network latency: Ensure good internet connection

Security Notes:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Tokens are stored locally in auth_tokens.json
- Only user's data is accessible after login
- All data transmission uses HTTPS ready
- Tokens auto-refresh before expiration
- Logout clears all local tokens

Support:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For issues or questions:
1. Check README.md in frontend-desktop folder
2. Review config.py settings
3. Check backend is running: http://localhost:8000
4. Look at error messages in console

Version: 1.0.0
Created: February 2026
Platform: Cross-platform (Windows, macOS, Linux)
"""

if __name__ == '__main__':
    print(__doc__)
