from rest_framework import permissions

class IsUliana(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.username == 'Uliana':
            return False
        return True
    
class IsBen(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if obj.location == 'Kazan' and request.user.username == 'Uliana':
            return False
        return True
    
class IsForecaster(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if hasattr(request.user, 'forecaster'):
            return True
        return False
    