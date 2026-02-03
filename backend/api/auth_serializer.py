from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    # valiadte is the method that responsible for returning the token pair (access and refresh tokens). 
    
    # validate method is overridden to include additional user information in the token response.
    def validate(self, attrs):
        
        # Call the superclass validate method to get the standard token data 
        data = super().validate(attrs)

        # Add custom user information to the response data
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
        }
        
        # Return the modified data with additional user info
        return data