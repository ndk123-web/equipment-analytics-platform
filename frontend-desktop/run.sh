#!/bin/bash

# Start script for the desktop application on Linux/macOS

echo "Starting Equipment Data Management Desktop Application..."
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Error creating virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
source venv/bin/activate

# Check if requirements are installed
pip show PyQt5 > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error installing dependencies"
        exit 1
    fi
fi

# Run the application
echo
echo "Starting application..."
python main.py

# Deactivate virtual environment when done
deactivate

read -p "Press enter to close this window..."
