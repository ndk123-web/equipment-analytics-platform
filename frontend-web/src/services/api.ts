import axios, { type AxiosInstance, type AxiosError } from 'axios';
import { useAuthStore } from '../store/authStore';
import type { AuthResponse, LoginRequest, SignupRequest } from '../types';
import type { UploadResponse } from '../types/upload';

// Create axios instance
const api: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Create axios instance for file uploads
const apiFormData: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api',
});

// Request interceptor - attach access token
api.interceptors.request.use(
  (config) => {
    const token = useAuthStore.getState().accessToken;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Request interceptor for FormData - attach access token
apiFormData.interceptors.request.use(
  (config) => {
    const token = useAuthStore.getState().accessToken;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor - handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    const originalRequest = error.config;

    // If 401 and not already retried
    if (error.response?.status === 401 && originalRequest && !('_retry' in originalRequest)) {
      (originalRequest as any)._retry = true;

      try {
        const refreshToken = useAuthStore.getState().refreshToken;
        if (refreshToken) {
          const response = await axios.post(
            'http://localhost:8000/api/auth/token/refresh/',
            { refresh: refreshToken }
          );

          const { access } = response.data;
          useAuthStore.getState().setTokens(access, refreshToken);

          // Retry original request with new token
          if (originalRequest.headers) {
            originalRequest.headers.Authorization = `Bearer ${access}`;
          }
          return api(originalRequest);
        }
      } catch (refreshError) {
        useAuthStore.getState().logout();
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

// Response interceptor for FormData - handle token refresh
apiFormData.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    const originalRequest = error.config;

    // If 401 and not already retried
    if (error.response?.status === 401 && originalRequest && !('_retry' in originalRequest)) {
      (originalRequest as any)._retry = true;

      try {
        const refreshToken = useAuthStore.getState().refreshToken;
        if (refreshToken) {
          const response = await axios.post(
            'http://localhost:8000/api/auth/token/refresh/',
            { refresh: refreshToken }
          );

          const { access } = response.data;
          useAuthStore.getState().setTokens(access, refreshToken);

          // Retry original request with new token
          if (originalRequest.headers) {
            originalRequest.headers.Authorization = `Bearer ${access}`;
          }
          return apiFormData(originalRequest);
        }
      } catch (refreshError) {
        useAuthStore.getState().logout();
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

// Auth API calls
export const authAPI = {
  login: async (credentials: LoginRequest): Promise<AuthResponse> => {
    const response = await api.post('/app1/token/', credentials);
    console.log("Login API response:", response.data);
    return response.data;
  },

  signup: async (data: SignupRequest): Promise<AuthResponse> => {
    const response = await api.post('/signup/', data);
    return response.data;
  },

  getProfile: async () => {
    const response = await api.get('/auth/me/');
    return response.data;
  },

  logout: async () => {
    try {
      await api.post('/auth/logout/');
    } catch (error) {
      // Error during logout is not critical
    }
  },
};

// File upload API calls
export const uploadAPI = {
  uploadCSV: async (file: File): Promise<UploadResponse> => {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await apiFormData.post('/web/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    console.log("Upload API response:", response.data);
    return response.data;
  },
};

export const fetchHistoryAPI = async (limit: number, offset: number) => {
  const response = await api.get(`/get-history?limit=${limit}&offset=${offset}`);
  console.log("Fetch History API response:", response.data);
  return response.data;
}

export default api;
