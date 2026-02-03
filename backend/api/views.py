# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializers import DatasetSerializer 
from .models import Dataset

# Create your views here.
# def testHome(request):
#     return HttpResponse("Hello I Am Ndk")

@api_view(["GET"])
@permission_classes([AllowAny])
def testHome(request):
    return Response({"message": "Hello I Am Ndk"})

@api_view(["POST"])
@permission_classes([AllowAny])
def signUp(request):
    
    username = request.data.get("username")
    password = request.data.get("password")
    
    if not username or not password:
        return Response({"error": "Username and password are required."}, status=400)
    
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists."}, status=400)
    
    user = User.objects.create_user(username=username, password=password)
    user.save()
    
    refresh = RefreshToken.for_user(user)
    access = AccessToken.for_user(user)
    
    return Response({
        "access": str(access),
        "refresh": str(refresh),
        "user": {
            "id": user.id,
            "username": user.username,
        }
    })
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def historyList(request):
    
    user = request.user 
    print("Authenticated user:", user.username)
    
    # get limit and offset from query params
    limit = request.GET.get("limit")
    offset = request.GET.get("offset")
    
    if not limit:
        limit = 5
    
    if not offset:
        offset = 0
    
    try:
        limit = int(limit)
        offset = int(offset)
    except ValueError:
        return Response({"error": "Invalid query parameters."}, status=400)
    except Exception as e:  
        return Response({"error": "Invalid query parameters."}, status=400)
    
    # fetch datasets for the user with pagination and returns queryset ordered by uploaded_at descending
    qs = (Dataset.objects.filter(uploaded_by=user).order_by("-uploaded_at"))
    
    # apply pagination 
    pagination_qs = qs[offset:offset+limit]
    
    # serialize the paginated queryset
    serializer = DatasetSerializer(pagination_qs, many=True)
    
    print("Serialized data:", serializer.data)
    
    # return response with count, limit, offset and serialized results
    return Response({
        "count": qs.count(),
        "limit": limit,
        "offset": offset,
        "results": serializer.data,
    })
    