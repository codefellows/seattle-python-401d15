from rest_framework import permissions

# New for lab 32
class IsPurchaserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.purchaser == request.user

