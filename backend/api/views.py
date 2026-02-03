# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes

# Create your views here.
# def testHome(request):
#     return HttpResponse("Hello I Am Ndk")

@api_view(["GET"])
@permission_classes([AllowAny])
def testHome(request):
    return Response({"message": "Hello I Am Ndk"})