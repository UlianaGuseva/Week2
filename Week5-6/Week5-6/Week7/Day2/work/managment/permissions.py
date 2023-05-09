from rest_framework import permissions

class IsDepartmentAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.admin == request.user
    