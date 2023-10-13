from rest_framework import permissions

class IsIngredientOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the ingredient
        return obj.user == request.user