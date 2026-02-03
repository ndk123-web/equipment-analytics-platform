from rest_framework import serializers
from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    # It means that the uploaded_by field will be read-only and will display the username of the user who uploaded the dataset.
    
    uploaded_by = serializers.ReadOnlyField(source='uploaded_by.username') 
    
    class Meta:
        model = Dataset
        fields = "__all__"