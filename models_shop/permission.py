from rest_framework.permissions import BasePermission
from .models import *

from rest_framework import permissions


class BlocklistPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Product.objects.filter(username=request.user.username).exists()
        return not blocked



class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user