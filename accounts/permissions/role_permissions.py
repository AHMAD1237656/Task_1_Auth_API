from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Sirf Admin access kar sakta hai.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "admin"
        )