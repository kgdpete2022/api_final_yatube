from rest_framework import permissions


class AuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    message = 'Операция разрешена только автору контента'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS 
            or request.user == obj.author
        )


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHOD
