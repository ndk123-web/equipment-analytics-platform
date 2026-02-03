import { useState } from 'react';
import { uploadAPI } from '../../services/api';

interface CSVUploadFormProps {
  onUploadSuccess?: (filename: string) => void;
}

export const CSVUploadForm: React.FC<CSVUploadFormProps> = ({ onUploadSuccess }) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadError, setUploadError] = useState<string | null>(null);
  const [uploadSuccess, setUploadSuccess] = useState<string | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    
    if (!file) {
      setSelectedFile(null);
      return;
    }

    // Validate file type
    if (!file.name.endsWith('.csv')) {
      setUploadError('Please select a CSV file');
      setSelectedFile(null);
      return;
    }

    // Validate file size (max 10MB)
    if (file.size > 10 * 1024 * 1024) {
      setUploadError('File size must be less than 10MB');
      setSelectedFile(null);
      return;
    }

    setSelectedFile(file);
    setUploadError(null);
    setUploadSuccess(null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setUploadError('Please select a file');
      return;
    }

    setIsUploading(true);
    setUploadError(null);

    try {
      await uploadAPI.uploadCSV(selectedFile);
      
      setUploadSuccess(`Successfully uploaded: ${selectedFile.name}`);
      setSelectedFile(null);
      
      // Reset file input
      const fileInput = document.getElementById('csv-file-input') as HTMLInputElement;
      if (fileInput) fileInput.value = '';

      if (onUploadSuccess) {
        onUploadSuccess(selectedFile.name);
      }

      // Clear success message after 3 seconds
      setTimeout(() => setUploadSuccess(null), 3000);
    } catch (error: any) {
      const errorMessage =
        error.response?.data?.error ||
        error.message ||
        'Upload failed. Please try again.';
      setUploadError(errorMessage);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-xl font-semibold text-gray-900 mb-4">📤 Upload CSV File</h2>
      
      <div className="space-y-4">
        {/* File Input */}
        <div>
          <label htmlFor="csv-file-input" className="block text-sm font-medium text-gray-700 mb-2">
            Select CSV File
          </label>
          <input
            id="csv-file-input"
            type="file"
            accept=".csv"
            onChange={handleFileChange}
            disabled={isUploading}
            className="block w-full text-sm text-gray-500
              file:mr-4 file:py-2 file:px-4
              file:rounded-full file:border-0
              file:text-sm file:font-semibold
              file:bg-blue-50 file:text-blue-700
              hover:file:bg-blue-100
              disabled:opacity-50"
          />
        </div>

        {/* File Info */}
        {selectedFile && (
          <div className="p-3 bg-blue-50 rounded-lg border border-blue-200">
            <p className="text-sm text-gray-700">
              <span className="font-semibold">Selected:</span> {selectedFile.name} ({(selectedFile.size / 1024).toFixed(2)} KB)
            </p>
          </div>
        )}

        {/* Error Message */}
        {uploadError && (
          <div className="p-3 bg-red-50 border border-red-200 rounded-lg">
            <p className="text-sm text-red-700">❌ {uploadError}</p>
          </div>
        )}

        {/* Success Message */}
        {uploadSuccess && (
          <div className="p-3 bg-green-50 border border-green-200 rounded-lg">
            <p className="text-sm text-green-700">✅ {uploadSuccess}</p>
          </div>
        )}

        {/* Upload Button */}
        <button
          onClick={handleUpload}
          disabled={!selectedFile || isUploading}
          className={`w-full py-2.5 px-4 font-semibold text-white rounded-lg transition ${
            selectedFile && !isUploading
              ? 'bg-blue-600 hover:bg-blue-700 active:bg-blue-800 cursor-pointer'
              : 'bg-gray-400 cursor-not-allowed'
          }`}
        >
          {isUploading ? 'Uploading...' : 'Upload CSV'}
        </button>

        {/* Helper text */}
        <p className="text-xs text-gray-500 text-center">
          Supported format: CSV only • Maximum file size: 10MB
        </p>
      </div>
    </div>
  );
};
