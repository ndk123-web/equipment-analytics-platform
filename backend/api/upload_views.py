from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from .serializers import DatasetSerializer
import pandas as pd 

@api_view(["POST"])
@permission_classes([IsAuthenticated]) # Only authenticated users can upload files and JWT is used 
def uploadWebFile(request):
    # Handle file upload logic here
    file = request.FILES.get('file')
    
    print("Its Web Upload File Api , if in future u want to change anything related to web upload , change here ")
    
    if not file:
        return Response({"error": "No file provided"}, status=400)
    
    if not file.name.endswith(".csv"):
        return Response({"error": "Only CSV files are supported"}, status=400)
    
    try:
        df = pd.read_csv(file)
    except Exception as e:
        return Response({"error": f"Failed to read CSV file: {str(e)}"}, status=400)
    
    total_records = len(df)
    if total_records == 0:
        return Response({"error": "CSV file is empty"}, status=400)
    
    avg_flowRate = df["FlowRate"].mean()
    avg_pressure = df["Pressure"].mean()
    avg_temperature = df["Temperature"].mean()
    
    equipment_distribution = df["Type"].value_counts().to_dict()
    
    serializer = DatasetSerializer(data={
        "name": file.name,
        "total_rows": total_records,
        "avg_usage_hours": avg_flowRate,
        "avg_power": avg_pressure,
        "equipment_distribution": equipment_distribution,
    })
    
    # raise exception=True will raise a 400 error if data is invalid
    serializer.is_valid(raise_exception=True)
    
    serializer.save(uploaded_by=request.user)
    
    # 201 because a resource is created
    # 200 is generic success 
    return Response(serializer.data, status=201)


def uploadDesktopFile(request):
    # Handle file upload logic here
    file = request.FILES.get('file')
    
    print("Its Desktop Upload File Api , if in future u want to change anything related to Desktop upload , change here ")
    
    if not file:
        return Response({"error": "No file provided"}, status=400)
    
    if not file.name.endswith(".csv"):
        return Response({"error": "Only CSV files are supported"}, status=400)
    
    try:
        df = pd.read_csv(file)
    except Exception as e:
        return Response({"error": f"Failed to read CSV file: {str(e)}"}, status=400)
    
    total_records = len(df)
    if total_records == 0:
        return Response({"error": "CSV file is empty"}, status=400)
    
    avg_flowRate = df["FlowRate"].mean()
    avg_pressure = df["Pressure"].mean()
    avg_temperature = df["Temperature"].mean()
    
    equipment_distribution = df["Type"].value_counts().to_dict()
    
    serializer = DatasetSerializer(data={
        "name": file.name,
        "total_rows": total_records,
        "avg_usage_hours": avg_flowRate,
        "avg_power": avg_pressure,
        "equipment_distribution": equipment_distribution,
    })
    
    # raise exception=True will raise a 400 error if data is invalid
    serializer.is_valid(raise_exception=True)
    
    serializer.save(uploaded_by=request.user)
    
    # 201 because a resource is created
    # 200 is generic success 
    return Response(serializer.data, status=201)

