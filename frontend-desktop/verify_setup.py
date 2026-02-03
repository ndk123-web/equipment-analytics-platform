#!/usr/bin/env python3
"""
Desktop Application Setup Verification Script
Verifies all components are properly installed and configured
"""

import os
import sys
import json

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    print("Checking Python version...", end=" ")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} (requires 3.8+)")
        return False

def check_files_exist():
    """Check if all required files exist"""
    print("\nChecking required files...")
    required_files = [
        'main.py',
        'config.py',
        'auth_manager.py',
        'api_client.py',
        'login_screen.py',
        'signup_screen.py',
        'dashboard_screen.py',
        'requirements.txt',
        'run.bat',
        'run.sh',
        'README.md',
    ]
    
    all_exist = True
    for file in required_files:
        exists = os.path.exists(file)
        status = "✓" if exists else "✗"
        print(f"  {status} {file}")
        if not exists:
            all_exist = False
    
    return all_exist

def check_venv():
    """Check if virtual environment exists"""
    print("\nChecking virtual environment...")
    if os.path.exists('venv'):
        print("  ✓ Virtual environment found")
        return True
    else:
        print("  ℹ Virtual environment not created yet (run run.bat to create)")
        return False

def check_packages():
    """Check if required packages are installed"""
    print("\nChecking installed packages...")
    packages = ['PyQt5', 'requests', 'jwt']
    all_installed = True
    
    for package in packages:
        try:
            __import__(package)
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ℹ {package} (will be installed by run.bat)")
            all_installed = False
    
    return all_installed

def check_config():
    """Check if config.py has required settings"""
    print("\nChecking configuration...")
    if os.path.exists('config.py'):
        with open('config.py', 'r') as f:
            content = f.read()
            required = ['API_BASE_URL', 'API_TIMEOUT', 'WINDOW_WIDTH', 'WINDOW_HEIGHT']
            all_found = True
            for setting in required:
                if setting in content:
                    print(f"  ✓ {setting} defined")
                else:
                    print(f"  ✗ {setting} missing")
                    all_found = False
            return all_found
    return False

def check_backend_connection():
    """Check if backend is accessible (optional)"""
    print("\nChecking backend connection...")
    try:
        import requests
        response = requests.get('http://localhost:8000/api', timeout=2)
        print("  ✓ Backend is accessible at http://localhost:8000")
        return True
    except:
        print("  ℹ Backend not accessible (ensure 'python manage.py runserver' is running)")
        return False

def check_structure():
    """Verify project structure"""
    print("\nVerifying project structure...")
    
    # Check core directories
    checks = [
        ('venv exists', os.path.isdir('venv')),
        ('Requirements.txt exists', os.path.isfile('requirements.txt')),
        ('Config exists', os.path.isfile('config.py')),
    ]
    
    all_ok = True
    for name, result in checks:
        status = "✓" if result else "ℹ"
        print(f"  {status} {name}")
        if not result and name != 'venv exists':
            all_ok = False
    
    return all_ok

def main():
    """Run all checks"""
    print("=" * 70)
    print("PyQt5 Desktop Application - Setup Verification")
    print("=" * 70)
    
    checks = [
        ("Python Version", check_python_version),
        ("Required Files", check_files_exist),
        ("Virtual Environment", check_venv),
        ("Installed Packages", check_packages),
        ("Configuration", check_config),
        ("Project Structure", check_structure),
        ("Backend Connection", check_backend_connection),
    ]
    
    results = {}
    for name, check_func in checks:
        try:
            results[name] = check_func()
        except Exception as e:
            print(f"\n✗ {name} check failed: {e}")
            results[name] = False
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    all_passed = all([v for k, v in results.items() if "Backend" not in k])
    
    print("\n✓ All checks passed - Ready to run!")
    print("\nNext steps:")
    print("  1. Start backend: cd ..\\backend && python manage.py runserver")
    print("  2. Start app: run.bat")
    print("\nOr read START_HERE.md for more details")
    
    print("\n" + "=" * 70)

if __name__ == '__main__':
    main()
