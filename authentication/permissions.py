from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status

def is_authenticated(request):
    if not request.user.is_authenticated:
        raise AuthenticationFailed(detail={'object':'authentication'
                                           ,'error':'Authentication is failed'}
                                           , code=status.HTTP_401_UNAUTHORIZED)
def is_role(request, role):
    if not request.user.role.name == role:
        raise AuthenticationFailed(detail={'object':'authentication'
                                           ,'error':'User does not have the required role'}
                                           , code=status.HTTP_403_FORBIDDEN)

class IsAuthenticated(BasePermission):
     def has_permission(self, request, view):
         is_authenticated(request)
         return True

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
         is_authenticated(request)
         is_role(request,'ADMIN')
         return True

class IsUser(BasePermission):
    def has_permission(self, request, view):
         is_authenticated(request)
         is_role(request,'USER')
         return True