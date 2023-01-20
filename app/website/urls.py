from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from accounts.views import AuthorSerializer

# router = routers.DefaultRouter()
# router.register('register', UserRegisterViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),

    path('api/register/', AuthorSerializer.as_view({
        'get': 'list',
        'post': 'create'
    }))
]
