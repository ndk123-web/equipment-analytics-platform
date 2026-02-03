"""Authentication manager for handling user session and tokens."""

import json
import os
from typing import Optional, Dict, Any
import requests
from config import API_BASE_URL, TOKEN_STORAGE_FILE, API_TIMEOUT


class AuthManager:
    """Manages authentication state and token refresh logic."""
    
    def __init__(self):
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self.user: Optional[Dict[str, Any]] = None
        self.load_tokens()
    
    def load_tokens(self) -> bool:
        """Load tokens from storage file if they exist."""
        if os.path.exists(TOKEN_STORAGE_FILE):
            try:
                with open(TOKEN_STORAGE_FILE, 'r') as f:
                    data = json.load(f)
                    self.access_token = data.get('access_token')
                    self.refresh_token = data.get('refresh_token')
                    self.user = data.get('user')
                    return True
            except Exception as e:
                print(f"Error loading tokens: {e}")
        return False
    
    def save_tokens(self) -> None:
        """Save tokens to storage file."""
        try:
            data = {
                'access_token': self.access_token,
                'refresh_token': self.refresh_token,
                'user': self.user
            }
            with open(TOKEN_STORAGE_FILE, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error saving tokens: {e}")
    
    def clear_tokens(self) -> None:
        """Clear tokens from memory and storage."""
        self.access_token = None
        self.refresh_token = None
        self.user = None
        if os.path.exists(TOKEN_STORAGE_FILE):
            os.remove(TOKEN_STORAGE_FILE)
    
    def set_tokens(self, access_token: str, refresh_token: str, user: Optional[Dict[str, Any]] = None) -> None:
        """Set tokens and optionally user data."""
        self.access_token = access_token
        self.refresh_token = refresh_token
        if user:
            self.user = user
        self.save_tokens()
    
    def is_authenticated(self) -> bool:
        """Check if user is authenticated."""
        return self.access_token is not None
    
    def get_headers(self) -> Dict[str, str]:
        """Get headers with authorization token."""
        headers = {'Content-Type': 'application/json'}
        if self.access_token:
            headers['Authorization'] = f'Bearer {self.access_token}'
        return headers
    
    def refresh_access_token(self) -> bool:
        """Refresh the access token using refresh token."""
        if not self.refresh_token:
            return False
        
        try:
            response = requests.post(
                f"{API_BASE_URL}/app1/token/refresh/",
                json={'refresh': self.refresh_token},
                timeout=API_TIMEOUT
            )
            
            if response.status_code == 200:
                data = response.json()
                self.access_token = data.get('access')
                self.save_tokens()
                return True
        except Exception as e:
            print(f"Error refreshing token: {e}")
        
        return False
    
    def request_with_retry(self, method: str, url: str, **kwargs) -> requests.Response:
        """Make a request with automatic token refresh on 401."""
        kwargs.setdefault('headers', {}).update(self.get_headers())
        kwargs.setdefault('timeout', API_TIMEOUT)
        
        response = requests.request(method, url, **kwargs)
        
        # If unauthorized and we have a refresh token, try to refresh
        if response.status_code == 401 and self.refresh_token:
            if self.refresh_access_token():
                # Retry the request with new token
                kwargs['headers'] = self.get_headers()
                response = requests.request(method, url, **kwargs)
        
        return response


# Global auth manager instance
auth_manager = AuthManager()
