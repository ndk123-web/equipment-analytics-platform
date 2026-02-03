@echo off
REM Start script for the desktop application on Windows

echo Starting Equipment Data Management Desktop Application...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error creating virtual environment
        exit /b 1
    )
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if requirements are installed
pip show PyQt5 >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error installing dependencies
        exit /b 1
    )
)

REM Run the application
echo.
echo Starting application...
python main.py

REM Deactivate virtual environment when done
deactivate

pause
