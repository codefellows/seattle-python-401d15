from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # STRETCH: lock down deletes???


        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
