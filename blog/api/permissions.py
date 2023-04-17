from rest_framework import permissions

class AuthorModifyOrReadonly(permissions.IsAuthenticatedOrReadOnly):
  
  def has_object_permission(self, request, views, obj):
    if request.method in permissions.SAFE_METHODS:
      return True

    return request.user == obj.author

class IsAdminUserForObject(permissions.IsAdminUser):
  
  def has_object_permission(self, request, view, obj):
      return bool(request.user and request.user.is_staff)