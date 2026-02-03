"""Signup screen for the desktop application."""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from api_client import APIClient
from auth_manager import auth_manager


class SignupScreen(QWidget):
    """Signup screen widget."""
    
    # Signal emitted when signup is successful
    signup_successful = pyqtSignal(dict)  # Passes user data
    switch_to_login = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI."""
        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Title
        title = QLabel("Create Account")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Fill in your details to create a new account")
        subtitle.setFont(QFont("Arial", 10))
        subtitle.setStyleSheet("color: #666;")
        layout.addWidget(subtitle)
        
        layout.addSpacing(15)
        
        # Username field
        username_label = QLabel("Username:")
        username_label.setFont(QFont("Arial", 10))
        layout.addWidget(username_label)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Choose a username")
        self.username_input.setMinimumHeight(40)
        layout.addWidget(self.username_input)
        
        # Email field
        email_label = QLabel("Email:")
        email_label.setFont(QFont("Arial", 10))
        layout.addWidget(email_label)
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email (optional)")
        self.email_input.setMinimumHeight(40)
        layout.addWidget(self.email_input)
        
        # First name field
        firstname_label = QLabel("First Name:")
        firstname_label.setFont(QFont("Arial", 10))
        layout.addWidget(firstname_label)
        
        self.firstname_input = QLineEdit()
        self.firstname_input.setPlaceholderText("Enter your first name (optional)")
        self.firstname_input.setMinimumHeight(40)
        layout.addWidget(self.firstname_input)
        
        # Last name field
        lastname_label = QLabel("Last Name:")
        lastname_label.setFont(QFont("Arial", 10))
        layout.addWidget(lastname_label)
        
        self.lastname_input = QLineEdit()
        self.lastname_input.setPlaceholderText("Enter your last name (optional)")
        self.lastname_input.setMinimumHeight(40)
        layout.addWidget(self.lastname_input)
        
        # Password field
        password_label = QLabel("Password:")
        password_label.setFont(QFont("Arial", 10))
        layout.addWidget(password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter a strong password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(40)
        layout.addWidget(self.password_input)
        
        # Confirm password field
        confirm_password_label = QLabel("Confirm Password:")
        confirm_password_label.setFont(QFont("Arial", 10))
        layout.addWidget(confirm_password_label)
        
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm your password")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setMinimumHeight(40)
        layout.addWidget(self.confirm_password_input)
        
        layout.addSpacing(10)
        
        # Signup button
        signup_btn = QPushButton("Create Account")
        signup_btn.setMinimumHeight(40)
        signup_btn.setFont(QFont("Arial", 11, QFont.Bold))
        signup_btn.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:pressed {
                background-color: #1e7e34;
            }
        """)
        signup_btn.clicked.connect(self.on_signup_clicked)
        layout.addWidget(signup_btn)
        
        layout.addSpacing(10)
        
        # Login link
        login_layout = QHBoxLayout()
        login_layout.addStretch()
        login_text = QLabel("Already have an account? ")
        login_text.setFont(QFont("Arial", 10))
        login_layout.addWidget(login_text)
        
        login_link = QPushButton("Log in")
        login_link.setStyleSheet("""
            QPushButton {
                color: #28a745;
                text-decoration: underline;
                border: none;
                background-color: transparent;
                font-weight: bold;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
        """)
        login_link.clicked.connect(self.switch_to_login.emit)
        login_layout.addWidget(login_link)
        login_layout.addStretch()
        
        layout.addLayout(login_layout)
        
        layout.addStretch()
        
        self.setLayout(layout)
    
    def on_signup_clicked(self):
        """Handle signup button click."""
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        confirm_password = self.confirm_password_input.text().strip()
        email = self.email_input.text().strip()
        first_name = self.firstname_input.text().strip()
        last_name = self.lastname_input.text().strip()
        
        # Validation
        if not username:
            QMessageBox.warning(self, "Validation Error", "Please enter username")
            return
        
        if not password:
            QMessageBox.warning(self, "Validation Error", "Please enter password")
            return
        
        if not confirm_password:
            QMessageBox.warning(self, "Validation Error", "Please confirm password")
            return
        
        if password != confirm_password:
            QMessageBox.warning(self, "Validation Error", "Passwords do not match")
            return
        
        if len(password) < 6:
            QMessageBox.warning(self, "Validation Error", "Password must be at least 6 characters")
            return
        
        try:
            # Make API call
            result = APIClient.signup(
                username=username,
                password=password,
                email=email if email else None,
                first_name=first_name if first_name else None,
                last_name=last_name if last_name else None
            )
            
            # Store tokens and user info
            auth_manager.set_tokens(
                result['access'],
                result['refresh'],
                result.get('user')
            )
            
            # Emit success signal
            self.signup_successful.emit(result.get('user', {}))
            
            # Clear inputs
            self.clear()
            
        except Exception as e:
            QMessageBox.critical(self, "Signup Failed", str(e))
    
    def clear(self):
        """Clear all input fields."""
        self.username_input.clear()
        self.email_input.clear()
        self.firstname_input.clear()
        self.lastname_input.clear()
        self.password_input.clear()
        self.confirm_password_input.clear()
