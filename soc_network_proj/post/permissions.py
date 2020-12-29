from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    # User may update/delete only own posts
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user