"""Main application entry point for the desktop application."""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from config import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE
from login_screen import LoginScreen
from signup_screen import SignupScreen
from dashboard_screen import DashboardScreen
from auth_manager import auth_manager


class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.check_auth_status()
    
    def init_ui(self):
        """Initialize the UI."""
        self.setWindowTitle(WINDOW_TITLE)
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # Set a nice font
        font = QFont("Arial", 10)
        self.setFont(font)
        
        # Create stacked widget for screen switching
        self.stacked_widget = QStackedWidget()
        
        # Create screens
        self.login_screen = LoginScreen()
        self.signup_screen = SignupScreen()
        
        # Add screens to stacked widget
        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.signup_screen)
        
        # Set login as initial screen
        self.stacked_widget.setCurrentWidget(self.login_screen)
        
        # Connect signals
        self.login_screen.login_successful.connect(self.on_login_success)
        self.login_screen.switch_to_signup.connect(self.show_signup)
        
        self.signup_screen.signup_successful.connect(self.on_signup_success)
        self.signup_screen.switch_to_login.connect(self.show_login)
        
        # Set central widget
        self.setCentralWidget(self.stacked_widget)
        
        # Style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
        """)
    
    def check_auth_status(self):
        """Check if user is already authenticated."""
        if auth_manager.is_authenticated():
            self.show_dashboard(auth_manager.user)
        else:
            self.show_login()
    
    def show_login(self):
        """Show login screen."""
        self.login_screen.clear()
        self.stacked_widget.setCurrentWidget(self.login_screen)
    
    def show_signup(self):
        """Show signup screen."""
        self.signup_screen.clear()
        self.stacked_widget.setCurrentWidget(self.signup_screen)
    
    def on_login_success(self, user_data):
        """Handle successful login."""
        self.show_dashboard(user_data)
    
    def on_signup_success(self, user_data):
        """Handle successful signup."""
        self.show_dashboard(user_data)
    
    def show_dashboard(self, user_data):
        """Show dashboard screen."""
        # Remove old dashboard if exists
        dashboard = None
        for i in range(self.stacked_widget.count()):
            widget = self.stacked_widget.widget(i)
            if isinstance(widget, DashboardScreen):
                dashboard = widget
                break
        
        if dashboard:
            self.stacked_widget.removeWidget(dashboard)
        
        # Create new dashboard
        self.dashboard_screen = DashboardScreen(user_data)
        self.dashboard_screen.logout_requested.connect(self.on_logout)
        self.stacked_widget.addWidget(self.dashboard_screen)
        self.stacked_widget.setCurrentWidget(self.dashboard_screen)
    
    def on_logout(self):
        """Handle logout."""
        # Remove dashboard
        dashboard = None
        for i in range(self.stacked_widget.count()):
            widget = self.stacked_widget.widget(i)
            if isinstance(widget, DashboardScreen):
                dashboard = widget
                break
        
        if dashboard:
            self.stacked_widget.removeWidget(dashboard)
        
        self.show_login()


def main():
    """Main entry point."""
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
