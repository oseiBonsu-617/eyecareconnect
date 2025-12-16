from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsExaminerOrReadOnly(BasePermission):
    """
    Allow read-only access to authenticated users.
    Only the examiner or admin can edit/delete.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions
        if request.method in SAFE_METHODS:
            return True

        # Admin can edit anything
        if request.user.role == "admin":
            return True

        # Only examiner can modify
        return obj.examiner == request.user
