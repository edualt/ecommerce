from rest_framework.permissions import BasePermission

class IsUser(BasePermission):

    def has_permission(self, request, view, obj):
        return obj.owner == request.user