
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', include('api.urls')),
    path('admin/', admin.site.urls),
    
]
