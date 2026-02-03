from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

from api.auth_views import CustomTokenObtainPairView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    
    path('api/app1/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/app1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
