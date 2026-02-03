"""API client for communicating with the backend."""

import requests
from typing import Optional, Dict, Any
from auth_manager import auth_manager
from config import API_BASE_URL, API_TIMEOUT


class APIClient:
    """Handles all API communication."""
    
    @staticmethod
    def login(username: str, password: str) -> Dict[str, Any]:
        """
        Login with username and password.
        
        Args:
            username: Username
            password: Password
        
        Returns:
            Dictionary with access token, refresh token, and user info
        """
        try:
            response = auth_manager.request_with_retry(
                'POST',
                f"{API_BASE_URL}/app1/token/",
                json={'username': username, 'password': password}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Login failed: {str(e)}")
    
    @staticmethod
    def signup(username: str, password: str, email: Optional[str] = None, 
               first_name: Optional[str] = None, last_name: Optional[str] = None) -> Dict[str, Any]:
        """
        Sign up a new user.
        
        Args:
            username: Username
            password: Password
            email: Email (optional)
            first_name: First name (optional)
            last_name: Last name (optional)
        
        Returns:
            Dictionary with access token, refresh token, and user info
        """
        try:
            data = {
                'username': username,
                'password': password
            }
            if email:
                data['email'] = email
            if first_name:
                data['first_name'] = first_name
            if last_name:
                data['last_name'] = last_name
            
            response = auth_manager.request_with_retry(
                'POST',
                f"{API_BASE_URL}/signup/",
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Signup failed: {str(e)}")
    
    @staticmethod
    def upload_file(file_path: str) -> Dict[str, Any]:
        """
        Upload a CSV file.
        
        Args:
            file_path: Path to the CSV file
        
        Returns:
            Dictionary with upload result
        """
        try:
            with open(file_path, 'rb') as f:
                files = {'file': (file_path, f, 'text/csv')}
                response = auth_manager.request_with_retry(
                    'POST',
                    f"{API_BASE_URL}/desktop/upload",
                    files=files
                )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Upload failed: {str(e)}")
        except IOError as e:
            raise Exception(f"File error: {str(e)}")
    
    @staticmethod
    def get_history(limit: int = 10, offset: int = 0) -> Dict[str, Any]:
        """
        Get upload history.
        
        Args:
            limit: Number of records to fetch
            offset: Offset for pagination
        
        Returns:
            Dictionary with history data
        """
        try:
            response = auth_manager.request_with_retry(
                'GET',
                f"{API_BASE_URL}/get-history/?limit={limit}&offset={offset}"
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Fetch history failed: {str(e)}")
    
    @staticmethod
    def logout() -> None:
        """Logout the user."""
        try:
            auth_manager.request_with_retry(
                'POST',
                f"{API_BASE_URL}/auth/logout/",
                json={}
            )
        except Exception as e:
            print(f"Error during logout: {e}")
        finally:
            auth_manager.clear_tokens()
