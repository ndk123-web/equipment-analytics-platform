export interface UploadHistory {
  id: string;
  filename: string;
  uploadedAt: string;
  size: number;
  status: 'success' | 'pending' | 'failed';
}

export interface UploadResponse {
  success: boolean;
  message: string;
  filename?: string;
  size?: number;
}
