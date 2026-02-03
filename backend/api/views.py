# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

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