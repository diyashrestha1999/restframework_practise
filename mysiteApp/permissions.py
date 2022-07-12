from rest_framework import permissions
from django.contrib.auth.models import User

from mysiteApp.models import SuperAdmin, Vendor


class SuperUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
                
            if SuperAdmin.objects.filter(owner=request.user).exists():
                return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
         