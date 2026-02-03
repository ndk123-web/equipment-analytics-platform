import { useMemo } from 'react';
import type { UploadHistory } from '../../types/upload';

interface UploadHistoryListProps {
  uploads: UploadHistory[];
  isLoading?: boolean;
}

export const UploadHistoryList: React.FC<UploadHistoryListProps> = ({
  uploads,
  isLoading = false,
}) => {
  // Get last 5 uploads
  const recentUploads = useMemo(() => {
    return uploads.slice(0, 5);
  }, [uploads]);

  if (isLoading) {
    return (
      <div className="bg-white rounded-xl shadow-md p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">📋 Upload History</h2>
        <div className="text-center py-8">
          <p className="text-gray-500">Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-xl font-semibold text-gray-900 mb-4">📋 Upload History</h2>

      {recentUploads.length === 0 ? (
        <div className="text-center py-8 text-gray-500">
          <p>No uploads yet. Start by uploading a CSV file above.</p>
        </div>
      ) : (
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-gray-200">
                <th className="text-left py-3 px-4 font-semibold text-gray-700">Filename</th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">Size</th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">Status</th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">Date</th>
              </tr>
            </thead>
            <tbody>
              {recentUploads.map((upload) => (
                <tr key={upload.id} className="border-b border-gray-100 hover:bg-gray-50 transition">
                  <td className="py-3 px-4 text-gray-900 font-medium">
                    <span className="flex items-center gap-2">
                      <span className="text-lg">📄</span>
                      {upload.filename}
                    </span>
                  </td>
                  <td className="py-3 px-4 text-gray-600">
                    {(upload.size / 1024).toFixed(2)} KB
                  </td>
                  <td className="py-3 px-4">
                    <span
                      className={`inline-flex items-center gap-1 px-3 py-1 rounded-full text-xs font-semibold ${
                        upload.status === 'success'
                          ? 'bg-green-100 text-green-700'
                          : upload.status === 'pending'
                          ? 'bg-yellow-100 text-yellow-700'
                          : 'bg-red-100 text-red-700'
                      }`}
                    >
                      {upload.status === 'success' && '✅'}
                      {upload.status === 'pending' && '⏳'}
                      {upload.status === 'failed' && '❌'}
                      {upload.status.charAt(0).toUpperCase() + upload.status.slice(1)}
                    </span>
                  </td>
                  <td className="py-3 px-4 text-gray-600">
                    {new Date(upload.uploadedAt).toLocaleDateString('en-US', {
                      year: 'numeric',
                      month: 'short',
                      day: 'numeric',
                      hour: '2-digit',
                      minute: '2-digit',
                    })}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {uploads.length > 5 && (
        <div className="mt-4 text-sm text-gray-500 text-center">
          Showing last 5 uploads out of {uploads.length} total
        </div>
      )}
    </div>
  );
};
