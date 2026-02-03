import { useState, useCallback, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { CSVUploadForm } from '../components/upload/CSVUploadForm';
import { AnalyticsCharts } from '../components/upload/AnalyticsCharts';
import { UploadHistoryList } from '../components/upload/UploadHistoryList';
import { useAuthStore } from '../store/authStore';
import type { UploadResponse } from '../types/upload';
import { fetchHistoryAPI } from '../services/api';

export const UploadDashboard = () => {
  const navigate = useNavigate();
  const { user, logout } = useAuthStore();
  const [uploadHistory, setUploadHistory] = useState<UploadResponse[]>([]);
  const [currentUpload, setCurrentUpload] = useState<UploadResponse | null>(null);
  const [totalCount, setTotalCount] = useState<number>(0);
  const [limit, setLimit] = useState<number>(5);
  const [offset, setOffset] = useState<number>(0);

  const handleUploadSuccess = useCallback((uploadData: UploadResponse) => {
    setCurrentUpload(uploadData);
    setUploadHistory((prev) => [uploadData, ...prev]);
  }, []);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  useEffect(() => {
    // Fetch upload history from API
    fetchHistoryAPI(limit, offset).then((response) => {
      // response is { count, limit, offset, results }
      setUploadHistory(response.results);
      setTotalCount(response.count);
      if (response.results.length > 0) {
        setCurrentUpload(response.results[0]);
      }
    }).catch((error) => {
      console.error('Error fetching upload history:', error);
    });
  }, [limit, offset]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <div>
            <h1 className="text-2xl font-bold text-gray-900">📊 Analytics Dashboard</h1>
            <p className="text-gray-600 text-sm">Welcome, {user?.username || 'User'}!</p>
          </div>
          <button
            onClick={handleLogout}
            className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition font-medium"
          >
            Logout
          </button>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
          {/* Upload Form - Takes less space */}
          <div className="lg:col-span-1">
            <CSVUploadForm onUploadSuccess={handleUploadSuccess} />
          </div>

          {/* Current Upload Info */}
          <div className="lg:col-span-2">
            {currentUpload ? (
              <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-6 border border-blue-200">
                <h3 className="text-lg font-semibold text-gray-900 mb-4">✅ Latest Upload</h3>
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                  <div>
                    <p className="text-gray-600 text-sm">File</p>
                    <p className="text-gray-900 font-semibold text-sm truncate">{currentUpload.name}</p>
                  </div>
                  <div>
                    <p className="text-gray-600 text-sm">Rows</p>
                    <p className="text-gray-900 font-semibold text-sm">{currentUpload.total_rows}</p>
                  </div>
                  <div>
                    <p className="text-gray-600 text-sm">Avg Power</p>
                    <p className="text-gray-900 font-semibold text-sm">{currentUpload.avg_power.toFixed(2)}</p>
                  </div>
                  <div>
                    <p className="text-gray-600 text-sm">Avg Hrs</p>
                    <p className="text-gray-900 font-semibold text-sm">{currentUpload.avg_usage_hours.toFixed(2)}</p>
                  </div>
                </div>
              </div>
            ) : (
              <div className="bg-gray-50 rounded-xl p-6 border border-gray-200 text-center">
                <p className="text-gray-500">Upload a CSV file to see latest statistics</p>
              </div>
            )}
          </div>
        </div>

        {/* Charts Section */}
        <div className="mb-8">
          <AnalyticsCharts uploadData={currentUpload} />
        </div>

        {/* Upload History */}
        <div>
          <UploadHistoryList uploads={uploadHistory} isLoading={false} totalCount={totalCount} />
        </div>
      </main>
    </div>
  );
};
