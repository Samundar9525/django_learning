from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('', include('acess_management.urls')),
    path('admin/', admin.site.urls),
]
