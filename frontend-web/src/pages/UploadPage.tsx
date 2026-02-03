import { useState, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { CSVUploadForm } from '../components/upload/CSVUploadForm';
import { UploadHistoryList } from '../components/upload/UploadHistoryList';
import type { UploadResponse } from '../types/upload';

// Mock upload history data
const MOCK_UPLOADS: UploadResponse[] = [
  {
    id: 1,
    name: 'sales_data_2024.csv',
    uploaded_by: 'admin',
    uploaded_at: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
    total_rows: 150,
    avg_usage_hours: 45.5,
    avg_power: 2850.75,
    equipment_distribution: { 'Motor A': 30, 'Motor B': 25, 'Generator': 40, 'Compressor': 20, 'Pump': 35 },
  },
  {
    id: 2,
    name: 'customer_list.csv',
    uploaded_by: 'admin',
    uploaded_at: new Date(Date.now() - 5 * 60 * 60 * 1000).toISOString(),
    total_rows: 200,
    avg_usage_hours: 52.3,
    avg_power: 3120.45,
    equipment_distribution: { 'Motor A': 45, 'Motor B': 35, 'Generator': 50 },
  },
  {
    id: 3,
    name: 'Q1_report.csv',
    uploaded_by: 'user',
    uploaded_at: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString(),
    total_rows: 300,
    avg_usage_hours: 38.7,
    avg_power: 2650.25,
    equipment_distribution: { 'Motor A': 60, 'Motor B': 50, 'Compressor': 40 },
  },
  {
    id: 4,
    name: 'inventory_backup.csv',
    uploaded_by: 'admin',
    uploaded_at: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toISOString(),
    total_rows: 250,
    avg_usage_hours: 48.9,
    avg_power: 2900.60,
    equipment_distribution: { 'Motor A': 55, 'Motor B': 40, 'Generator': 35, 'Pump': 25 },
  },
  {
    id: 5,
    name: 'user_accounts.csv',
    uploaded_by: 'user',
    uploaded_at: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString(),
    total_rows: 180,
    avg_usage_hours: 42.1,
    avg_power: 3000.80,
    equipment_distribution: { 'Motor A': 50, 'Motor B': 30, 'Generator': 45, 'Compressor': 35, 'Pump': 40 },
  },
];

export const UploadPage = () => {
  const navigate = useNavigate();
  const { user, logout } = useAuthStore();
  const [uploadHistory, setUploadHistory] = useState<UploadResponse[]>(MOCK_UPLOADS);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const handleUploadSuccess = useCallback((uploadData: UploadResponse) => {
    setUploadHistory((prev) => [uploadData, ...prev]);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">
                📊 CSV Upload Dashboard
              </h1>
              <p className="text-gray-600 mt-1">
                Welcome, <span className="font-semibold">{user?.username || 'User'}</span>
              </p>
            </div>
            <button
              onClick={handleLogout}
              className="px-6 py-2.5 bg-red-600 text-white rounded-lg hover:bg-red-700 transition font-medium"
            >
              Logout
            </button>
          </div>
        </div>

        {/* Main Content - Grid Layout */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Upload Section - Spans 1 column on desktop */}
          <div className="lg:col-span-1">
            <CSVUploadForm onUploadSuccess={handleUploadSuccess} />
          </div>

          {/* History Section - Spans 2 columns on desktop */}
          <div className="lg:col-span-2">
            <UploadHistoryList uploads={uploadHistory} isLoading={false} />
          </div>
        </div>

        {/* Info Box */}
        <div className="bg-blue-50 border border-blue-200 rounded-xl p-6 mt-6">
          <h3 className="font-semibold text-blue-900 mb-2">ℹ️ Upload Guidelines</h3>
          <ul className="text-sm text-blue-800 space-y-1">
            <li>✓ Only CSV files are accepted</li>
            <li>✓ Maximum file size is 10MB</li>
            <li>✓ Files are authenticated via Bearer token</li>
            <li>✓ Upload history shows your last 5 uploads</li>
          </ul>
        </div>
      </div>
    </div>
  );
};
