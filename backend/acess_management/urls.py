from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='acess_management'),
    path('', views.userData, name='acess_management'),
    path('users/', views.userData, name='acess_management'),
    path('fetch_data/<int:id>/', views.fetchUserData, name='acess_management'),
    path('updateUser/', views.updateUserData, name='acess_management'),
    path('delete_User/<int:id>/', views.deleteUser, name='acess_management'),
]