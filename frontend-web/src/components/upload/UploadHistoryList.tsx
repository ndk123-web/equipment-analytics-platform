import { useMemo } from 'react';
import type { UploadResponse } from '../../types/upload';

interface UploadHistoryListProps {
  uploads: UploadResponse[];
  isLoading?: boolean;
  totalCount?: number;
}

export const UploadHistoryList: React.FC<UploadHistoryListProps> = ({
  uploads,
  isLoading = false,
  totalCount = 0,
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
          <div className="animate-spin rounded-full h-8 w-8 border-4 border-blue-200 border-t-blue-600 mx-auto"></div>
          <p className="text-gray-500 mt-4">Loading...</p>
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
                <th className="text-left py-3 px-4 font-semibold text-gray-700">Rows</th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">Uploaded By</th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">Date</th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">Avg Power</th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">Avg Hours</th>
              </tr>
            </thead>
            <tbody>
              {recentUploads.map((upload) => (
                <tr key={upload.id} className="border-b border-gray-100 hover:bg-gray-50 transition">
                  <td className="py-3 px-4 text-gray-900 font-medium">
                    <span className="flex items-center gap-2">
                      <span className="text-lg">📄</span>
                      {upload.name}
                    </span>
                  </td>
                  <td className="py-3 px-4 text-gray-600">{upload.total_rows}</td>
                  <td className="py-3 px-4 text-gray-600">{upload.uploaded_by}</td>
                  <td className="py-3 px-4 text-gray-600 text-xs">
                    {new Date(upload.uploaded_at).toLocaleDateString('en-US', {
                      year: 'numeric',
                      month: 'short',
                      day: 'numeric',
                      hour: '2-digit',
                      minute: '2-digit',
                    })}
                  </td>
                  <td className="py-3 px-4 text-gray-700">{upload.avg_power.toFixed(2)}</td>
                  <td className="py-3 px-4 text-gray-700">{upload.avg_usage_hours.toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {totalCount > uploads.length && (
        <div className="mt-4 text-sm text-gray-500 text-center">
          Showing {uploads.length} out of {totalCount} uploads
        </div>
      )}
      {totalCount === 0 && uploads.length === 0 && (
        <div className="mt-4 text-sm text-gray-500 text-center">
          No uploads available
        </div>
      )}
    </div>
  );
};
