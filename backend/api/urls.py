from django.urls import path
from .views import testHome 
from .upload_views import uploadWebFile, uploadDesktopFile

urlpatterns = [
    path('', testHome),
    path('web/upload', uploadWebFile), # POST 
    path('desktop/upload', uploadDesktopFile), # POST
]