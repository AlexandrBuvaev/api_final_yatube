from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Ограничение, которое позволяет редактировать,
    частично редактировать и удалять посты только авторам 
    этих постов.      
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        return obj.author == request.user