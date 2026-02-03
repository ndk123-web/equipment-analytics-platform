"""Analytics screen with matplotlib visualizations."""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QComboBox, QMessageBox, QScrollArea
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from api_client import APIClient
import json


class AnalyticsScreen(QWidget):
    """Analytics screen with charts and visualizations."""
    
    back_requested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.history_data = []
        self.init_ui()
        self.load_analytics_data()
    
    def init_ui(self):
        """Initialize the UI."""
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Header
        header_layout = QHBoxLayout()
        title = QLabel("Analytics & Visualizations")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        header_layout.addWidget(title)
        header_layout.addStretch()
        
        back_btn = QPushButton("Back")
        back_btn.setMinimumWidth(80)
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        back_btn.clicked.connect(self.back_requested.emit)
        header_layout.addWidget(back_btn)
        layout.addLayout(header_layout)
        
        # Chart selection dropdown
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Select Chart:"))
        self.chart_combo = QComboBox()
        self.chart_combo.addItems([
            "Equipment Distribution (Latest)",
            "Average Values (All Uploads)",
            "Equipment Type Trends",
            "Upload Statistics"
        ])
        self.chart_combo.currentIndexChanged.connect(self.refresh_chart)
        filter_layout.addWidget(self.chart_combo)
        filter_layout.addStretch()
        layout.addLayout(filter_layout)
        
        # Chart area
        self.chart_figure = Figure(figsize=(12, 6), dpi=100)
        self.chart_canvas = FigureCanvas(self.chart_figure)
        layout.addWidget(self.chart_canvas)
        
        self.setLayout(layout)
    
    def load_analytics_data(self):
        """Load all history data for analytics."""
        try:
            # Load all data (with high limit)
            data = APIClient.get_history(limit=1000, offset=0)
            self.history_data = data.get('results', [])
            self.refresh_chart()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load analytics: {str(e)}")
    
    def refresh_chart(self):
        """Refresh the chart based on selection."""
        self.chart_figure.clear()
        chart_type = self.chart_combo.currentText()
        
        try:
            if "Equipment Distribution" in chart_type:
                self.plot_equipment_distribution()
            elif "Average Values" in chart_type:
                self.plot_average_values()
            elif "Equipment Type Trends" in chart_type:
                self.plot_equipment_trends()
            elif "Upload Statistics" in chart_type:
                self.plot_upload_stats()
            
            self.chart_canvas.draw()
        except Exception as e:
            self.chart_figure.text(0.5, 0.5, f"Error: {str(e)}", 
                                  ha='center', va='center', fontsize=12)
            self.chart_canvas.draw()
    
    def plot_equipment_distribution(self):
        """Plot pie chart of equipment distribution from latest upload."""
        if not self.history_data:
            self.chart_figure.text(0.5, 0.5, "No data available", 
                                  ha='center', va='center', fontsize=14)
            return
        
        # Get latest upload
        latest = self.history_data[0]
        equipment_dist = latest.get('equipment_distribution', {})
        
        if not equipment_dist:
            self.chart_figure.text(0.5, 0.5, "No equipment distribution data", 
                                  ha='center', va='center', fontsize=14)
            return
        
        ax = self.chart_figure.add_subplot(111)
        
        # Convert to lists
        labels = list(equipment_dist.keys())
        sizes = list(equipment_dist.values())
        
        # Create pie chart
        colors = plt.cm.Set3(range(len(labels)))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        ax.set_title(f"Equipment Distribution\n({latest.get('name', 'Latest Upload')})", 
                    fontsize=12, fontweight='bold')
    
    def plot_average_values(self):
        """Plot bar chart of average values across all uploads."""
        if not self.history_data:
            self.chart_figure.text(0.5, 0.5, "No data available", 
                                  ha='center', va='center', fontsize=14)
            return
        
        # Extract data
        filenames = [r.get('name', f"Upload {i+1}")[:15] for i, r in enumerate(self.history_data[:10])]
        flowrates = [r.get('avg_usage_hours', 0) for r in self.history_data[:10]]
        pressures = [r.get('avg_power', 0) for r in self.history_data[:10]]
        
        ax = self.chart_figure.add_subplot(111)
        
        # Create grouped bar chart
        x = range(len(filenames))
        width = 0.35
        
        bars1 = ax.bar([i - width/2 for i in x], flowrates, width, label='Avg FlowRate', color='#3498db')
        bars2 = ax.bar([i + width/2 for i in x], pressures, width, label='Avg Power', color='#e74c3c')
        
        ax.set_xlabel('Uploads', fontweight='bold')
        ax.set_ylabel('Value', fontweight='bold')
        ax.set_title('Average Values Across Uploads (Last 10)', fontsize=12, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(filenames, rotation=45, ha='right')
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        self.chart_figure.tight_layout()
    
    def plot_equipment_trends(self):
        """Plot equipment type trends over uploads."""
        if not self.history_data:
            self.chart_figure.text(0.5, 0.5, "No data available", 
                                  ha='center', va='center', fontsize=14)
            return
        
        # Collect equipment types and their counts
        equipment_types = {}
        for upload in self.history_data[:15]:  # Last 15 uploads
            dist = upload.get('equipment_distribution', {})
            for equipment, count in dist.items():
                if equipment not in equipment_types:
                    equipment_types[equipment] = []
                equipment_types[equipment].append(count)
        
        if not equipment_types:
            self.chart_figure.text(0.5, 0.5, "No equipment data", 
                                  ha='center', va='center', fontsize=14)
            return
        
        ax = self.chart_figure.add_subplot(111)
        
        # Plot lines for each equipment type
        for equipment, counts in equipment_types.items():
            ax.plot(range(len(counts)), counts, marker='o', label=equipment, linewidth=2)
        
        ax.set_xlabel('Upload Order (Recent →)', fontweight='bold')
        ax.set_ylabel('Count', fontweight='bold')
        ax.set_title('Equipment Type Trends Over Time', fontsize=12, fontweight='bold')
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3)
        
        self.chart_figure.tight_layout()
    
    def plot_upload_stats(self):
        """Plot upload statistics."""
        if not self.history_data:
            self.chart_figure.text(0.5, 0.5, "No data available", 
                                  ha='center', va='center', fontsize=14)
            return
        
        # Extract statistics
        total_uploads = len(self.history_data)
        total_records = sum([r.get('total_rows', 0) for r in self.history_data])
        avg_flowrate = sum([r.get('avg_usage_hours', 0) for r in self.history_data]) / total_uploads if total_uploads > 0 else 0
        avg_power = sum([r.get('avg_power', 0) for r in self.history_data]) / total_uploads if total_uploads > 0 else 0
        
        # Create figure with subplots
        ax = self.chart_figure.add_subplot(111)
        
        # Statistics text
        stats_text = f"""
        UPLOAD STATISTICS
        ═══════════════════════════════════════
        
        Total Uploads:                    {total_uploads}
        
        Total Records Uploaded:           {total_records:,}
        
        Average FlowRate (All):           {avg_flowrate:.2f}
        
        Average Power (All):              {avg_power:.2f}
        
        Average Records/Upload:           {total_records/total_uploads:.0f} records
        
        Latest Upload:                    {self.history_data[0].get('name', 'N/A')}
        """
        
        ax.text(0.5, 0.5, stats_text, transform=ax.transAxes,
               fontsize=11, verticalalignment='center', horizontalalignment='center',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
               family='monospace')
        ax.axis('off')
    
    def export_data(self):
        """Export analytics data to file (future feature)."""
        pass
