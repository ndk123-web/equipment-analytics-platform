# Equipment Data Management - Desktop Application

A PyQt5-based desktop application for managing equipment data with user authentication and CSV file uploads.

## Features

✅ **User Authentication**
- Login with username and password
- Signup with email and name
- JWT token-based authentication
- Automatic token refresh

✅ **File Management**
- Upload CSV files with equipment data
- File validation (CSV format only)
- Data analysis (calculate averages)

✅ **Upload History**
- View all uploaded files
- Pagination through history
- Display file statistics

## System Requirements

- Python 3.8 or higher
- Windows/macOS/Linux
- Backend server running at `http://localhost:8000`

## Installation

### 1. Create Virtual Environment

```bash
# Navigate to frontend-desktop directory
cd frontend-desktop

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Edit `config.py` to customize:

- `API_BASE_URL`: Backend API endpoint (default: `http://localhost:8000/api`)
- `WINDOW_WIDTH` / `WINDOW_HEIGHT`: Window dimensions
- `WINDOW_TITLE`: Application title

## Running the Application

### Start the Application

```bash
python main.py
```

### Expected Backend Endpoints

The application expects these endpoints on your Django backend:

- `POST /api/app1/token/` - Login
- `POST /api/signup/` - User signup
- `POST /api/desktop/upload` - File upload
- `GET /api/get-history/` - Fetch upload history
- `POST /api/auth/token/refresh/` - Refresh access token

## File Structure

```
frontend-desktop/
├── main.py                 # Application entry point
├── config.py              # Configuration settings
├── auth_manager.py        # Authentication and token management
├── api_client.py          # API communication
├── login_screen.py        # Login UI
├── signup_screen.py       # Signup UI
├── dashboard_screen.py    # Dashboard UI with upload & history
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## CSV File Format

The uploaded CSV file should contain the following columns:

- `Type`: Equipment type
- `FlowRate`: Flow rate value
- `Pressure`: Pressure value
- `Temperature`: Temperature value

Example:
```
Type,FlowRate,Pressure,Temperature
Pump,45.2,100.5,25.3
Valve,32.1,98.2,24.8
Motor,50.3,102.1,26.1
```

## Features Detail

### Login Screen
- Username/password authentication
- Link to signup page
- Error handling and validation

### Signup Screen
- Create new user account
- Optional email, first name, last name
- Password confirmation
- Link to login page

### Dashboard
- Welcome message with username
- Two main tabs: Upload and History

#### Upload Tab
- File browser to select CSV files
- Upload button with status
- File validation
- Success/error messages with statistics

#### History Tab
- Table displaying all uploaded files
- Columns: Filename, Records, Avg FlowRate, Avg Pressure, Equipment Distribution, Date
- Pagination controls (Previous/Next)
- Page indicator

### Token Management
- Automatic token refresh on 401 errors
- Persistent token storage in `auth_tokens.json`
- Secure logout with token cleanup

## Troubleshooting

### Backend Connection Issues
- Ensure Django backend is running on `http://localhost:8000`
- Check `config.py` for correct `API_BASE_URL`
- Verify CORS headers are enabled in Django

### File Upload Issues
- Ensure file is in CSV format
- Check CSV columns match expected names
- Verify file is not empty
- Check file permissions

### Authentication Issues
- Clear `auth_tokens.json` if you have token issues
- Restart the application
- Ensure backend is accessible

## Development Notes

- Uses PyQt5 for UI (Pure Python, cross-platform)
- Requests library for HTTP communication
- JWT tokens for authentication
- Local JSON file for token persistence

## Building Executable

To create a standalone executable, use PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

This will create an executable in the `dist/` directory.

## License

This project is part of the FOSSE Internship program.

---

**Version**: 1.0.0
**Created**: February 2026
