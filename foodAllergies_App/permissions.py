from rest_framework import permissions

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_staff or request.user.is_authenticated
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update']:
            return True
        elif view.action == 'destroy':
            return bool(request.user.is_superuser)
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update']:
            return obj.user == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return bool(request.user.is_superuser)
        else:
            return False

class RetrieveOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'retrieve':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):

        if view.action =='retrieve':
            return True
        else:
            return False
        
class FoodAllergyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return bool(request.user.is_staff)
        elif view.action in ['retrieve', 'update', 'partial_update']:
            return True
        elif view.action == 'destroy':
            return bool(request.user.is_superuser)
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update']:
            return request.user.is_staff
        elif view.action == 'destroy':
            return bool(request.user.is_superuser)
        else:
            return False

class FoodPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return bool(request.user.is_staff)
        elif view.action in ['retrieve', 'update', 'partial_update']:
            return True
        elif view.action == 'destroy':
            return bool(request.user.is_superuser)
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update']:
            return request.user.is_staff
        elif view.action == 'destroy':
            return bool(request.user.is_superuser)
        else:
            return False
        

class AllergyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return bool(request.user.is_staff)
        elif view.action in ['retrieve', 'update', 'partial_update']:
            return True
        elif view.action == 'destroy':
            return bool(request.user.is_superuser)
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update']:
            return request.user.is_staff
        elif view.action == 'destroy':
            return bool(request.user.is_superuser)
        else:
            return False


class CategoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return bool(request.user.is_staff)
        elif view.action in ['retrieve', 'update', 'partial_update']:
            return True
        elif view.action == 'destroy':
            return bool(request.user.is_superuser)
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update']:
            return request.user.is_staff
        elif view.action == 'destroy':
            return bool(request.user.is_superuser)
        else:
            return False