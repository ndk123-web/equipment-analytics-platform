// Auth related types
export interface User {
  id: string;
  username: string;
  email?: string;
  first_name?: string;
  last_name?: string;
}

export interface LoginRequest {
  username: string;
  password: string;
}

export interface SignupRequest {
  username: string;
  password: string;
  confirm_password?: string;
  first_name?: string;
  last_name?: string;
}

export interface AuthResponse {
  access: string;
  refresh: string;
  user: User;
}

export interface ErrorResponse {
  error: string;
  message?: string;
}
