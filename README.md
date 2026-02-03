# 🚀 Equipment Data Management System

Complete full-stack application with Django backend, React web frontend, and PyQt5 desktop frontend.

## 📑 Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Backend Setup (Django)](#backend-setup-django)
4. [Frontend Web Setup (React)](#frontend-web-setup-react)
5. [Frontend Desktop Setup (PyQt5)](#frontend-desktop-setup-pyqt5)
6. [Running All Services](#running-all-services)
7. [API Endpoints](#api-endpoints)
8. [Features](#features)
9. [Troubleshooting](#troubleshooting)

---

## 🎯 Project Overview

A comprehensive equipment data management system with three interfaces:

- **Backend API**: Django REST Framework with JWT authentication
- **Web Frontend**: Modern React SPA with TypeScript
- **Desktop App**: Cross-platform PyQt5 desktop application
- **Features**: User auth, CSV upload, data analytics, upload history

**Technology Stack**:
- Backend: Django, DRF, SQLite, JWT
- Web: React, TypeScript, Vite, Tailwind CSS, Zustand
- Desktop: PyQt5, Python, Matplotlib
- Database: SQLite

---

## 📂 Project Structure

```
FOSSE-Internship/
├── backend/                    # Django REST API
│   ├── manage.py
│   ├── requirements.txt
│   ├── db.sqlite3
│   ├── core/                   # Project settings
│   ├── api/                    # Main API app
│   ├── myenv/                  # Virtual environment
│   └── README.md
│
├── frontend-web/               # React SPA
│   ├── package.json
│   ├── src/
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── README.md
│
├── frontend-desktop/           # PyQt5 Desktop App
│   ├── main.py
│   ├── requirements.txt
│   ├── venv/                   # Virtual environment
│   ├── run.bat
│   ├── run.sh
│   └── README.md
│
└── README.md                   # This file
```

---

## 🔧 Backend Setup (Django)

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

#### 1. Navigate to Backend Directory
```bash
cd backend
```

#### 2. Create & Activate Virtual Environment
```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Create Superuser (Optional - for admin access)
```bash
python manage.py createsuperuser
# Follow prompts to create admin user
```

#### 6. Start Development Server
```bash
python manage.py runserver
```

Server will run at: `http://localhost:8000`

### Verify Backend is Running
- Visit: http://localhost:8000/api/
- Admin panel: http://localhost:8000/admin/

### Project Structure
```
backend/
├── core/
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL routing
│   └── wsgi.py
├── api/
│   ├── models.py            # Database models
│   ├── serializers.py       # DRF serializers
│   ├── views.py             # API views
│   ├── upload_views.py      # File upload handlers
│   ├── auth_views.py        # Authentication views
│   └── urls.py              # API routes
├── manage.py
└── requirements.txt
```

### Key API Endpoints
- `POST /api/app1/token/` - Login
- `POST /api/app1/token/refresh/` - Refresh token
- `POST /api/signup/` - Register user
- `POST /api/web/upload` - Web file upload
- `POST /api/desktop/upload` - Desktop file upload
- `GET /api/get-history/` - Get upload history

---

## 💻 Frontend Web Setup (React)

### Prerequisites
- Node.js 16+ (includes npm)

### Installation Steps

#### 1. Navigate to Frontend-Web Directory
```bash
cd frontend-web
```

#### 2. Install Dependencies
```bash
npm install
```

#### 3. Start Development Server
```bash
npm run dev
```

App will run at: `http://localhost:5173`

### Available Scripts

```bash
# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint
```

### Project Structure
```
frontend-web/
├── src/
│   ├── components/
│   │   ├── auth/             # Login/Signup components
│   │   ├── upload/           # Upload components
│   │   └── ProtectedRoute.tsx
│   ├── pages/
│   │   ├── LoginPage.tsx
│   │   ├── SignupPage.tsx
│   │   ├── DashboardPage.tsx
│   │   └── UploadPage.tsx
│   ├── services/
│   │   └── api.ts            # API client
│   ├── store/
│   │   └── authStore.ts      # Zustand store
│   ├── types/
│   │   └── index.ts
│   ├── App.tsx
│   └── main.tsx
├── package.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

### Environment Setup

The web frontend automatically connects to `http://localhost:8000/api` by default.

To change backend URL, modify in `src/services/api.ts`:
```typescript
const api: AxiosInstance = axios.create({
  baseURL: 'http://your-backend-url/api',
  // ...
});
```

### Features
- React 19 with TypeScript
- JWT authentication with auto-refresh
- CSV file upload
- Upload history with pagination
- Responsive UI with Tailwind CSS
- Form validation with Zod

---

## 🖥️ Frontend Desktop Setup (PyQt5)

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

#### 1. Navigate to Frontend-Desktop Directory
```bash
cd frontend-desktop
```

#### 2. Quick Start (Windows) - Double-click file
```bash
run.bat
```

#### 2. Quick Start (Linux/macOS)
```bash
chmod +x run.sh
./run.sh
```

#### 3. Manual Setup

**Create & Activate Virtual Environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**Install Dependencies:**
```bash
pip install -r requirements.txt
```

**Run Application:**
```bash
python main.py
```

### Project Structure
```
frontend-desktop/
├── main.py                 # Application entry point
├── config.py               # Configuration settings
├── auth_manager.py         # Authentication & token management
├── api_client.py           # API communication
├── login_screen.py         # Login UI
├── signup_screen.py        # Signup UI
├── dashboard_screen.py     # Dashboard UI
├── analytics_screen.py     # Analytics with Matplotlib
├── requirements.txt        # Python dependencies
├── run.bat                 # Windows launcher
├── run.sh                  # Linux/macOS launcher
└── venv/                   # Virtual environment
```

### Features
- Cross-platform desktop app (Windows, macOS, Linux)
- JWT authentication
- CSV file upload with validation
- Upload history with pagination
- Analytics dashboard
- Matplotlib charts and visualizations
- Automatic token refresh
- Session persistence

### Configuration

Edit `config.py` to customize:
```python
API_BASE_URL = "http://localhost:8000/api"  # Backend URL
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
API_TIMEOUT = 10
TOKEN_STORAGE_FILE = "auth_tokens.json"
```

---

## 🚀 Running All Services

### Quick Start (All 3 in Separate Terminals)

**Terminal 1 - Backend:**
```bash
cd backend
myenv\Scripts\activate  # Windows: myenv\Scripts\activate | Mac/Linux: source myenv/bin/activate
python manage.py runserver
```

**Terminal 2 - Web Frontend:**
```bash
cd frontend-web
npm run dev
```

**Terminal 3 - Desktop Frontend:**
```bash
cd frontend-desktop
run.bat  # Windows: run.bat | Mac/Linux: ./run.sh
```

### Service Endpoints

| Service | URL | Purpose |
|---------|-----|---------|
| Backend API | http://localhost:8000 | REST API server |
| Backend Admin | http://localhost:8000/admin | Django admin panel |
| Web Frontend | http://localhost:5173 | React SPA |
| Desktop App | N/A | Standalone PyQt5 app |

---

## 📡 API Endpoints

### Authentication
```
POST   /api/app1/token/              Login
POST   /api/app1/token/refresh/      Refresh token
POST   /api/signup/                  Register user
GET    /api/auth/me/                 Get user profile
```

### File Upload
```
POST   /api/web/upload               Upload CSV (web)
POST   /api/desktop/upload           Upload CSV (desktop)
```

### History
```
GET    /api/get-history/             Get upload history (paginated)
```

### Query Parameters
```
/api/get-history/?limit=10&offset=0  Pagination parameters
```

---

## ✨ Features

### 🔐 Authentication
- Username/password login
- User registration
- JWT tokens (access + refresh)
- Automatic token refresh on expiration
- Secure logout
- Session persistence (web) / Local storage (desktop)

### 📤 File Upload
- CSV file upload with validation
- Automatic data analysis:
  - Record count
  - Average FlowRate
  - Average Power/Pressure
  - Equipment distribution
- Error handling and validation

### 📊 Upload History
- View all uploaded files
- Pagination (10 items per page)
- Sort by upload date
- Display statistics

### 📈 Analytics (Desktop Only)
- Pie chart: Equipment distribution
- Bar chart: Average values comparison
- Line chart: Equipment trends
- Statistics summary

---

## 📋 CSV File Format

Required columns (case-sensitive):

```csv
Type,Flowrate,Pressure,Temperature
Pump,120,5.2,110
Compressor,95,8.4,95
Valve,60,4.1,105
```

### Column Requirements
- **Type** (string): Equipment type name
- **Flowrate** (number): Flow rate value
- **Pressure** (number): Pressure value
- **Temperature** (number): Temperature value

---

## 🔄 Development Workflow

### Making Changes

**Backend:**
1. Edit code in `backend/`
2. Restart Django server
3. Changes take effect immediately

**Web Frontend:**
1. Edit code in `frontend-web/src/`
2. Vite hot-reloads automatically
3. Check browser for updates

**Desktop:**
1. Edit code in `frontend-desktop/`
2. Restart `python main.py`
3. Changes take effect on restart

### Adding Dependencies

**Backend:**
```bash
cd backend
pip install package-name
pip freeze > requirements.txt
```

**Web Frontend:**
```bash
cd frontend-web
npm install package-name
```

**Desktop:**
```bash
cd frontend-desktop
venv\Scripts\pip install package-name
pip freeze > requirements.txt
```

---

## 🆘 Troubleshooting

### Backend Issues

**"Port 8000 already in use"**
```bash
# Kill process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8000 | xargs kill -9
```

**"ModuleNotFoundError"**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

**"Database locked"**
```bash
# Delete and recreate database
rm db.sqlite3
python manage.py migrate
```

### Web Frontend Issues

**"Cannot GET /"**
- Ensure backend is running on http://localhost:8000
- Check `API_BASE_URL` in `src/services/api.ts`

**"Dependencies not installing"**
```bash
# Clear npm cache
npm cache clean --force
npm install
```

**Port 5173 already in use**
```bash
# Kill process or use different port
npm run dev -- --port 3000
```

### Desktop App Issues

**"Cannot connect to backend"**
- Start backend: `cd backend && python manage.py runserver`
- Check `API_BASE_URL` in `config.py`
- Verify backend is accessible: http://localhost:8000

**"PyQt5 import error"**
```bash
cd frontend-desktop
pip install -r requirements.txt
```

**"CSV upload fails"**
- Check column names: Type, Flowrate, Pressure, Temperature
- File must be .csv format
- File must not be empty

**Application won't start**
```bash
# Delete persistent data and try again
rm auth_tokens.json
python main.py
```

### General Issues

**"Cannot connect to backend"**
- Ensure all services are running
- Check firewall settings
- Verify ports are not blocked

**"Login fails"**
- Check username/password
- Create new account via signup
- Backend server running?

**"File upload fails"**
- Verify CSV format and columns
- Check file permissions
- Ensure file is not corrupted

---

## 📚 Additional Resources

### Documentation Files
- `backend/README.md` - Backend specific instructions
- `frontend-web/README.md` - Web frontend instructions
- `frontend-desktop/README.md` - Desktop app instructions
- `frontend-desktop/DEPLOYMENT_GUIDE.py` - Detailed deployment guide
- `frontend-desktop/API_REFERENCE.py` - Complete API documentation

### Technologies Used

**Backend:**
- Django 6.0.1
- Django REST Framework 3.16.1
- Simple JWT 5.5.1
- Pandas 3.0.0
- SQLite3

**Web Frontend:**
- React 19.2.0
- TypeScript 5.9.3
- Vite 7.2.4
- Tailwind CSS 4.1.18
- Axios 1.13.4
- Zustand 5.0.11

**Desktop:**
- PyQt5 5.15.11
- Requests 2.31.0
- Matplotlib 3.8.2
- Python 3.8+

---

## 📞 Quick Reference

### Start Everything (PowerShell - Windows)
```powershell
# Terminal 1
cd backend; .\myenv\Scripts\Activate.ps1; python manage.py runserver

# Terminal 2
cd frontend-web; npm run dev

# Terminal 3
cd frontend-desktop; .\run.bat
```

### Start Everything (Bash - Linux/macOS)
```bash
# Terminal 1
cd backend && source myenv/bin/activate && python manage.py runserver

# Terminal 2
cd frontend-web && npm run dev

# Terminal 3
cd frontend-desktop && ./run.sh
```

### Database Reset (Backend)
```bash
cd backend
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Build for Production

**Web Frontend:**
```bash
cd frontend-web
npm run build
# Output in dist/
```

**Desktop (Create .exe):**
```bash
cd frontend-desktop
pip install pyinstaller
pyinstaller --onefile --windowed main.py
# Output in dist/
```

---

## 📝 Version Information

- **Created**: February 2026
- **Backend**: Django 6.0.1
- **Web**: React 19.2.0
- **Desktop**: PyQt5 5.15.11
- **Python**: 3.8+
- **Node.js**: 16+

---

## ✅ Next Steps

1. **Backend**: `cd backend && python manage.py runserver`
2. **Web**: `cd frontend-web && npm run dev`
3. **Desktop**: `cd frontend-desktop && run.bat` (or `./run.sh`)
4. Create user account via signup
5. Upload CSV files
6. View analytics and history

---

## 🎉 You're All Set!

Now you have a complete full-stack application running on three different frontends!

### Happy Coding! 🚀

For detailed information on each component, refer to the individual README files in each folder.

---

**Last Updated**: February 3, 2026
