"""Dashboard screen for the desktop application."""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
    QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox,
    QTabWidget, QScrollArea, QHeaderView
)
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtGui import QFont
from api_client import APIClient
from auth_manager import auth_manager


class UploadWorker:
    """Worker for file upload in background."""
    pass


class DashboardScreen(QWidget):
    """Dashboard screen widget."""
    
    logout_requested = pyqtSignal()
    
    def __init__(self, user_data=None, parent=None):
        super().__init__(parent)
        self.user_data = user_data or {}
        self.current_page = 0
        self.init_ui()
        self.load_history()
    
    def init_ui(self):
        """Initialize the UI."""
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # Top bar with user info and logout
        top_layout = QHBoxLayout()
        
        username = self.user_data.get('username', 'User')
        user_label = QLabel(f"Welcome, {username}!")
        user_label.setFont(QFont("Arial", 14, QFont.Bold))
        top_layout.addWidget(user_label)
        
        top_layout.addStretch()
        
        logout_btn = QPushButton("Logout")
        logout_btn.setMinimumWidth(100)
        logout_btn.setMinimumHeight(35)
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
            QPushButton:pressed {
                background-color: #bd2130;
            }
        """)
        logout_btn.clicked.connect(self.on_logout_clicked)
        top_layout.addWidget(logout_btn)
        
        layout.addLayout(top_layout)
        
        # Tab widget
        tab_widget = QTabWidget()
        tab_widget.setFont(QFont("Arial", 10))
        
        # Upload tab
        upload_widget = self.create_upload_tab()
        tab_widget.addTab(upload_widget, "Upload File")
        
        # History tab
        history_widget = self.create_history_tab()
        tab_widget.addTab(history_widget, "Upload History")
        
        layout.addWidget(tab_widget)
        
        self.setLayout(layout)
    
    def create_upload_tab(self):
        """Create the file upload tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Instructions
        instructions = QLabel("Select a CSV file to upload")
        instructions.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(instructions)
        
        description = QLabel(
            "The CSV file should contain columns: Type, FlowRate, Pressure, Temperature"
        )
        description.setFont(QFont("Arial", 10))
        description.setStyleSheet("color: #666;")
        layout.addWidget(description)
        
        layout.addSpacing(20)
        
        # File selection area
        file_layout = QHBoxLayout()
        
        self.file_path_label = QLabel("No file selected")
        self.file_path_label.setFont(QFont("Arial", 10))
        self.file_path_label.setStyleSheet("color: #666; padding: 10px; background-color: #f5f5f5; border-radius: 5px;")
        file_layout.addWidget(self.file_path_label)
        
        browse_btn = QPushButton("Browse")
        browse_btn.setMinimumWidth(100)
        browse_btn.setMinimumHeight(35)
        browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        browse_btn.clicked.connect(self.browse_file)
        file_layout.addWidget(browse_btn)
        
        layout.addLayout(file_layout)
        
        layout.addSpacing(10)
        
        # Upload button
        self.upload_btn = QPushButton("Upload File")
        self.upload_btn.setMinimumHeight(40)
        self.upload_btn.setFont(QFont("Arial", 11, QFont.Bold))
        self.upload_btn.setEnabled(False)
        self.upload_btn.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover:!disabled {
                background-color: #0056b3;
            }
            QPushButton:disabled {
                background-color: #ccc;
                color: #999;
            }
        """)
        self.upload_btn.clicked.connect(self.on_upload_clicked)
        layout.addWidget(self.upload_btn)
        
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
    
    def create_history_tab(self):
        """Create the upload history tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("Upload History")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(title)
        
        # Table
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(6)
        self.history_table.setHorizontalHeaderLabels([
            "File Name", "Total Rows", "Avg FlowRate", "Avg Power", "Equipment Types", "Date"
        ])
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.history_table.setStyleSheet("""
            QTableWidget {
                gridline-color: #ddd;
                background-color: white;
            }
            QHeaderView::section {
                background-color: #f5f5f5;
                padding: 5px;
                border: 1px solid #ddd;
                font-weight: bold;
            }
        """)
        layout.addWidget(self.history_table)
        
        # Pagination buttons
        pagination_layout = QHBoxLayout()
        pagination_layout.addStretch()
        
        self.prev_btn = QPushButton("Previous")
        self.prev_btn.setMinimumWidth(100)
        self.prev_btn.clicked.connect(self.previous_page)
        self.prev_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover:!disabled {
                background-color: #5a6268;
            }
            QPushButton:disabled {
                background-color: #ccc;
                color: #999;
            }
        """)
        pagination_layout.addWidget(self.prev_btn)
        
        self.page_label = QLabel("Page 1")
        self.page_label.setFont(QFont("Arial", 10))
        pagination_layout.addWidget(self.page_label)
        
        self.next_btn = QPushButton("Next")
        self.next_btn.setMinimumWidth(100)
        self.next_btn.clicked.connect(self.next_page)
        self.next_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover:!disabled {
                background-color: #5a6268;
            }
            QPushButton:disabled {
                background-color: #ccc;
                color: #999;
            }
        """)
        pagination_layout.addWidget(self.next_btn)
        
        pagination_layout.addStretch()
        
        layout.addLayout(pagination_layout)
        
        widget.setLayout(layout)
        return widget
    
    def browse_file(self):
        """Open file browser to select a CSV file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)"
        )
        
        if file_path:
            self.selected_file_path = file_path
            self.file_path_label.setText(file_path)
            self.upload_btn.setEnabled(True)
    
    def on_upload_clicked(self):
        """Handle file upload."""
        if not hasattr(self, 'selected_file_path'):
            QMessageBox.warning(self, "Error", "No file selected")
            return
        
        self.upload_btn.setEnabled(False)
        self.upload_btn.setText("Uploading...")
        
        try:
            result = APIClient.upload_file(self.selected_file_path)
            QMessageBox.information(
                self,
                "Success",
                f"File uploaded successfully!\n\n"
                f"Records: {result.get('total_rows', 'N/A')}\n"
                f"Avg FlowRate: {result.get('avg_usage_hours', 'N/A'):.2f}\n"
                f"Avg Power (Pressure): {result.get('avg_power', 'N/A'):.2f}"
            )
            
            # Refresh history
            self.current_page = 0
            self.load_history()
            
            # Reset file selection
            self.file_path_label.setText("No file selected")
            self.selected_file_path = None
            
        except Exception as e:
            QMessageBox.critical(self, "Upload Failed", str(e))
        finally:
            self.upload_btn.setEnabled(True)
            self.upload_btn.setText("Upload File")
    
    def load_history(self):
        """Load upload history from API."""
        try:
            limit = 10
            offset = self.current_page * limit
            data = APIClient.get_history(limit, offset)
            
            # Clear table
            self.history_table.setRowCount(0)
            
            # Populate table
            records = data.get('results', [])
            for row_idx, record in enumerate(records):
                self.history_table.insertRow(row_idx)
                
                self.history_table.setItem(row_idx, 0, QTableWidgetItem(record.get('name', 'N/A')))
                self.history_table.setItem(row_idx, 1, QTableWidgetItem(str(record.get('total_rows', 'N/A'))))
                self.history_table.setItem(row_idx, 2, QTableWidgetItem(f"{float(record.get('avg_usage_hours', 0)):.2f}"))
                self.history_table.setItem(row_idx, 3, QTableWidgetItem(f"{float(record.get('avg_power', 0)):.2f}"))
                
                # Equipment distribution - format nicely
                equipment_dist = record.get('equipment_distribution', {})
                if isinstance(equipment_dist, dict):
                    dist_str = ", ".join([f"{k}: {v}" for k, v in equipment_dist.items()])
                else:
                    dist_str = str(equipment_dist)
                self.history_table.setItem(row_idx, 4, QTableWidgetItem(dist_str))
                
                # Date
                uploaded_at = record.get('uploaded_at', 'N/A')
                if uploaded_at != 'N/A':
                    uploaded_at = uploaded_at[:10]  # Format: YYYY-MM-DD
                self.history_table.setItem(row_idx, 5, QTableWidgetItem(uploaded_at))
            
            # Update pagination
            total = data.get('count', 0)
            limit = data.get('limit', 10)
            total_pages = (total + limit - 1) // limit if total > 0 else 1
            self.page_label.setText(f"Page {self.current_page + 1} of {total_pages}")
            
            self.prev_btn.setEnabled(self.current_page > 0)
            self.next_btn.setEnabled(self.current_page < total_pages - 1)
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load history: {str(e)}")
    
    def previous_page(self):
        """Go to previous page."""
        if self.current_page > 0:
            self.current_page -= 1
            self.load_history()
    
    def next_page(self):
        """Go to next page."""
        self.current_page += 1
        self.load_history()
    
    def on_logout_clicked(self):
        """Handle logout."""
        reply = QMessageBox.question(
            self,
            "Logout",
            "Are you sure you want to logout?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            APIClient.logout()
            self.logout_requested.emit()
