"""
PROJECT STRUCTURE & FILE GUIDE
==============================

Complete guide to all files in the PyQt5 Desktop Application
for Equipment Data Management.

ROOT DIRECTORY: frontend-desktop/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CORE APPLICATION FILES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

main.py (Application Entry Point)
- Purpose: Main application window and screen management
- Responsibilities:
  * Initialize QApplication
  * Create main window
  * Manage screen transitions (Login → Signup → Dashboard)
  * Handle authentication status check
  * Connect signals between screens
- Key Classes:
  * MainWindow: Central application window inheriting QMainWindow
- Key Methods:
  * check_auth_status(): Check if already logged in
  * show_login(): Switch to login screen
  * show_signup(): Switch to signup screen
  * show_dashboard(): Switch to dashboard
  * on_login_success(): Handle successful login
  * on_logout(): Handle logout
- Usage: python main.py

config.py (Configuration Settings)
- Purpose: Centralized configuration management
- Settings:
  * API_BASE_URL: Backend API endpoint
  * API_TIMEOUT: Request timeout duration
  * TOKEN_STORAGE_FILE: Local token storage location
  * WINDOW_WIDTH/HEIGHT: Application window size
  * WINDOW_TITLE: Window title
- Usage: Imported by other modules
- Modification: Edit to change backend URL or window size

auth_manager.py (Authentication & Token Management)
- Purpose: Handle all authentication logic and token persistence
- Key Classes:
  * AuthManager: Manages user session and JWT tokens
- Key Methods:
  * load_tokens(): Load saved tokens from file
  * save_tokens(): Save tokens to file
  * clear_tokens(): Clear all tokens
  * set_tokens(): Set and persist tokens
  * is_authenticated(): Check if user is logged in
  * get_headers(): Get HTTP headers with token
  * refresh_access_token(): Refresh token using refresh token
  * request_with_retry(): Make requests with auto-retry on 401
- Global Instance: auth_manager (imported in API calls)
- Features:
  * Automatic token refresh on 401 errors
  * Persistent token storage
  * Secure logout

api_client.py (API Communication)
- Purpose: Handle all backend API requests
- Key Classes:
  * APIClient: Static class for API operations
- Key Methods:
  * login(username, password): User login
  * signup(username, password, ...): User registration
  * upload_file(file_path): Upload CSV file
  * get_history(limit, offset): Fetch upload history
  * logout(): User logout
- Dependencies: auth_manager, config, requests
- Error Handling: Raises Exception with descriptive messages
- Features:
  * Token-based authentication
  * Automatic retry on token refresh
  * Proper error messages

UI SCREEN FILES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

login_screen.py (Login User Interface)
- Purpose: Provide login UI and handle user login
- Key Classes:
  * LoginScreen: QWidget for login interface
- Signals:
  * login_successful: Emitted on successful login
  * switch_to_signup: Emitted when user clicks signup link
- Components:
  * Username input field
  * Password input field
  * Login button
  * Signup link
- Features:
  * Input validation
  * Error message display
  * Loading state indication
  * Clear on logout
- Usage: Added to main window's stacked widget

signup_screen.py (Signup User Interface)
- Purpose: Provide signup UI and handle user registration
- Key Classes:
  * SignupScreen: QWidget for signup interface
- Signals:
  * signup_successful: Emitted on successful signup
  * switch_to_login: Emitted when user clicks login link
- Components:
  * Username input
  * Email input (optional)
  * First name input (optional)
  * Last name input (optional)
  * Password input
  * Confirm password input
  * Create account button
  * Login link
- Features:
  * Password confirmation matching
  * Minimum password length check
  * Comprehensive validation
  * Error messages
- Usage: Added to main window's stacked widget

dashboard_screen.py (Main Dashboard Interface)
- Purpose: Provide post-login dashboard with upload and history
- Key Classes:
  * DashboardScreen: QWidget for main dashboard
  * UploadWorker: Placeholder for background operations (future)
- Signals:
  * logout_requested: Emitted on logout
- Tabs:
  1. Upload Tab:
     * File browser
     * Selected file display
     * Upload button
     * Success/error messages
  2. History Tab:
     * Upload history table
     * Pagination controls
     * Formatted data display
- Features:
  * User welcome message
  * Logout button
  * File upload with validation
  * History pagination
  * Table with equipment distribution
- Methods:
  * create_upload_tab(): Create upload UI
  * create_history_tab(): Create history UI
  * browse_file(): Open file browser
  * on_upload_clicked(): Handle file upload
  * load_history(): Fetch and display history
  * previous_page(): Go to previous page
  * next_page(): Go to next page

DOCUMENTATION FILES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

README.md (User Documentation)
- Purpose: Quick start guide and feature overview
- Contents:
  * Installation steps
  * Configuration options
  * Running instructions
  * Feature descriptions
  * CSV format
  * Troubleshooting

DEPLOYMENT_GUIDE.py (Deployment Instructions)
- Purpose: Comprehensive deployment and setup guide
- Contents:
  * Prerequisites and requirements
  * Quick start for all platforms
  * Manual installation steps
  * Feature details
  * API endpoints overview
  * CSV format example
  * Configuration guide
  * Troubleshooting tips
  * Building executables
  * File structure
  * Performance tips
  * Security notes

API_REFERENCE.py (API Documentation)
- Purpose: Complete API reference and examples
- Contents:
  * All API endpoints with details
  * Request/response formats
  * Data models
  * Error codes
  * Python code examples
  * Token management
  * Caching information
  * Limitations

PROJECT_STRUCTURE.py (This File)
- Purpose: Document all project files
- Contents: This comprehensive guide

SETUP.py (Quick Setup Info)
- Purpose: Quick reference for setup
- Contents: Basic installation and setup info

CONFIGURATION & DEPENDENCIES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

requirements.txt (Python Dependencies)
- Purpose: List all required Python packages
- Contents:
  * PyQt5>=5.15.2 - GUI framework
  * requests==2.31.0 - HTTP client
  * PyJWT==2.11.0 - JWT token handling
- Usage: pip install -r requirements.txt
- Notes: Pre-built wheels to avoid build tools requirement

.gitignore (Git Ignore Patterns)
- Purpose: Exclude unnecessary files from git
- Ignores:
  * __pycache__ directories
  * *.pyc compiled files
  * venv/ virtual environment
  * auth_tokens.json (sensitive data)
  * .vscode, .idea (IDE files)
  * build/ and dist/ (build artifacts)

STARTUP SCRIPTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

run.bat (Windows Startup Script)
- Purpose: Easy application startup on Windows
- Features:
  * Auto-create virtual environment
  * Auto-install dependencies
  * Start application
  * Deactivate environment on exit
- Usage: Double-click run.bat

run.sh (Linux/macOS Startup Script)
- Purpose: Easy application startup on Linux/macOS
- Features:
  * Same as run.bat for Unix systems
  * Make executable: chmod +x run.sh
  * Run: ./run.sh or bash run.sh
- Usage: ./run.sh

GENERATED FILES (Created at Runtime):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

auth_tokens.json (NOT in repository)
- Purpose: Store user session tokens locally
- Contents:
  {
    "access_token": "JWT token",
    "refresh_token": "JWT token",
    "user": {
      "id": number,
      "username": "string"
    }
  }
- Security: Gitignored, never commit to repo
- Deleted on logout
- Created on successful login

venv/ (Virtual Environment - NOT in repository)
- Purpose: Isolated Python environment
- Contents: Python packages and interpreter
- Creation: python -m venv venv
- Gitignored: Never commit to repo
- Size: ~200MB after package installation

FILE RELATIONSHIPS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dependency Graph:
main.py
├── config.py (for settings)
├── auth_manager.py (store tokens)
├── login_screen.py
│   └── api_client.py
│       └── auth_manager.py
├── signup_screen.py
│   └── api_client.py
│       └── auth_manager.py
└── dashboard_screen.py
    └── api_client.py
        └── auth_manager.py

Data Flow:
User Input → Screen UI → API Client → Auth Manager → Backend API
                    ↑           ↓
                  Signals    Response
                    ↓           ↓
            Next Screen ← Store Tokens

EDITING GUIDELINES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

To Add New Features:
1. Backend API: Add endpoints in Django
2. API Client: Add methods in api_client.py
3. Auth Manager: Add token/auth logic if needed
4. UI: Create/modify screen files
5. Main: Add screen and signal connections

To Change Backend URL:
1. Edit config.py: API_BASE_URL setting
2. Restart application

To Modify UI:
1. Edit corresponding screen file (login/signup/dashboard)
2. Edit stylesheet strings for colors/fonts
3. Restart application

To Add CSV Columns:
1. Update backend upload handlers
2. Update CSV format documentation
3. Update error validation logic

PERFORMANCE NOTES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Startup: ~2-3 seconds (init PyQt5 and check auth)
- Login: ~1-2 seconds (API call + token refresh)
- Upload: Depends on file size (100MB ~5-10 seconds)
- History: ~1-2 seconds (API call + table render)
- Token Refresh: ~500ms (automatic, transparent)

Size Notes:
- Application size: ~5MB (without dependencies)
- Full install with PyQt5: ~500MB (venv)
- Executable: ~100MB+ (with PyInstaller)

SECURITY NOTES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Tokens stored locally in auth_tokens.json
- Only accessible to current user
- Deleted on logout
- HTTPS ready (use HTTPS in production)
- No password caching (only in memory during login)
- Tokens auto-refresh before expiration
- Automatic logout on token expiration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TOTAL FILE COUNT: 14 files
- Python: 7 files (main, config, auth, api, 3 screens)
- Documentation: 4 files (README, guides, API ref, this file)
- Config: 2 files (requirements, gitignore)
- Scripts: 2 files (run.bat, run.sh)

TOTAL LINES OF CODE: ~1500+ lines
EXTERNAL DEPENDENCIES: 3 (PyQt5, requests, PyJWT)
PYTHON VERSION: 3.8+
"""

if __name__ == '__main__':
    print(__doc__)
