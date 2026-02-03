import { useState, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { CSVUploadForm } from '../components/upload/CSVUploadForm';
import { UploadHistoryList } from '../components/upload/UploadHistoryList';
import type { UploadHistory } from '../types/upload';

// Mock upload history data
const MOCK_UPLOADS: UploadHistory[] = [
  {
    id: '1',
    filename: 'sales_data_2024.csv',
    uploadedAt: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
    size: 2048,
    status: 'success',
  },
  {
    id: '2',
    filename: 'customer_list.csv',
    uploadedAt: new Date(Date.now() - 5 * 60 * 60 * 1000).toISOString(),
    size: 4096,
    status: 'success',
  },
  {
    id: '3',
    filename: 'Q1_report.csv',
    uploadedAt: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString(),
    size: 1536,
    status: 'success',
  },
  {
    id: '4',
    filename: 'inventory_backup.csv',
    uploadedAt: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toISOString(),
    size: 5120,
    status: 'success',
  },
  {
    id: '5',
    filename: 'user_accounts.csv',
    uploadedAt: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString(),
    size: 3072,
    status: 'success',
  },
];

export const UploadPage = () => {
  const navigate = useNavigate();
  const { user, logout } = useAuthStore();
  const [uploadHistory, setUploadHistory] = useState<UploadHistory[]>(MOCK_UPLOADS);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const handleUploadSuccess = useCallback((filename: string) => {
    // Add new upload to history
    const newUpload: UploadHistory = {
      id: Date.now().toString(),
      filename,
      uploadedAt: new Date().toISOString(),
      size: Math.floor(Math.random() * 5000) + 512, // Mock size
      status: 'success',
    };

    setUploadHistory((prev) => [newUpload, ...prev]);
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
            <UploadHistoryList uploads={uploadHistory} />
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
