from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('roles', RoleListViews.as_view()),
    path('roles', RolesCreateView.as_view()),
    path('roles/<int:pk>', RolesUpdateView.as_view()),
    path('roles/destroy/<int:pk>', RolesDestroyView.as_view()),
    path('roles/retrieve/<int:pk>', RolesRetrieveView.as_view()),
    
    path('auth/register', AuthRegisterView.as_view()),
    path('auth/login', AuthLoginView.as_view()),
]