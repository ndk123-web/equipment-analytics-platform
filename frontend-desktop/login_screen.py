"""Login screen for the desktop application."""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QMessageBox, QStackedWidget
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from api_client import APIClient
from auth_manager import auth_manager


class LoginScreen(QWidget):
    """Login screen widget."""
    
    # Signal emitted when login is successful
    login_successful = pyqtSignal(dict)  # Passes user data
    switch_to_signup = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI."""
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Title
        title = QLabel("Login")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Enter your credentials to access your account")
        subtitle.setFont(QFont("Arial", 10))
        subtitle.setStyleSheet("color: #666;")
        layout.addWidget(subtitle)
        
        layout.addSpacing(20)
        
        # Username field
        username_label = QLabel("Username:")
        username_label.setFont(QFont("Arial", 10))
        layout.addWidget(username_label)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setMinimumHeight(40)
        layout.addWidget(self.username_input)
        
        # Password field
        password_label = QLabel("Password:")
        password_label.setFont(QFont("Arial", 10))
        layout.addWidget(password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(40)
        layout.addWidget(self.password_input)
        
        layout.addSpacing(10)
        
        # Login button
        login_btn = QPushButton("Login")
        login_btn.setMinimumHeight(40)
        login_btn.setFont(QFont("Arial", 11, QFont.Bold))
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004085;
            }
        """)
        login_btn.clicked.connect(self.on_login_clicked)
        layout.addWidget(login_btn)
        
        layout.addSpacing(10)
        
        # Signup link
        signup_layout = QHBoxLayout()
        signup_layout.addStretch()
        signup_text = QLabel("Don't have an account? ")
        signup_text.setFont(QFont("Arial", 10))
        signup_layout.addWidget(signup_text)
        
        signup_link = QPushButton("Sign up")
        signup_link.setStyleSheet("""
            QPushButton {
                color: #007bff;
                text-decoration: underline;
                border: none;
                background-color: transparent;
                font-weight: bold;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
        """)
        signup_link.clicked.connect(self.switch_to_signup.emit)
        signup_layout.addWidget(signup_link)
        signup_layout.addStretch()
        
        layout.addLayout(signup_layout)
        
        layout.addStretch()
        
        self.setLayout(layout)
    
    def on_login_clicked(self):
        """Handle login button click."""
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username:
            QMessageBox.warning(self, "Validation Error", "Please enter username")
            return
        
        if not password:
            QMessageBox.warning(self, "Validation Error", "Please enter password")
            return
        
        # Show loading state
        self.show_loading(True)
        
        try:
            # Make API call
            result = APIClient.login(username, password)
            
            # Store tokens and user info
            auth_manager.set_tokens(
                result['access'],
                result['refresh'],
                result.get('user')
            )
            
            # Emit success signal
            self.login_successful.emit(result.get('user', {}))
            
            # Clear inputs
            self.username_input.clear()
            self.password_input.clear()
            
        except Exception as e:
            QMessageBox.critical(self, "Login Failed", str(e))
        finally:
            self.show_loading(False)
    
    def show_loading(self, is_loading: bool):
        """Show/hide loading state."""
        # This can be extended to show a loading indicator
        pass
    
    def clear(self):
        """Clear all input fields."""
        self.username_input.clear()
        self.password_input.clear()
