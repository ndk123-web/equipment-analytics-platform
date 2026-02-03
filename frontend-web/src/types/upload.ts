export interface UploadResponse {
  id: number;
  name: string;
  uploaded_by: string;
  uploaded_at: string;
  total_rows: number;
  avg_usage_hours: number;
  avg_power: number;
  equipment_distribution: Record<string, number>;
}

export interface PaginatedResponse {
  count: number;
  limit: number;
  offset: number;
  results: UploadResponse[];
}

export interface UploadHistory {
  id: string;
  filename: string;
  uploadedAt: string;
  size: number;
  status: 'success' | 'pending' | 'failed';
}
