from django.contrib import admin
from django.urls import path, include


from accounts.views import AuthorViewSet
from items.views import ItemViewSet




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),

    path('api/register/', AuthorViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/items/', ItemViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }))
]
