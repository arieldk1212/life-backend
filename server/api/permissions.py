from rest_framework import permissions

AllowAnyPermission = permissions.AllowAny

AdminUserPermission = permissions.IsAdminUser

AuthenticatedOrReadOnlyPermission = permissions.IsAuthenticatedOrReadOnly


