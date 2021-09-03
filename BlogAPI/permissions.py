from rest_framework import permissions

#ruxsatlar admin yoki faqat reader yoki post yaratgan user
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #faqat get boshqalarga
        if request.method in permissions.SAFE_METHODS:
            return True
        #post faqat adminga
        return obj.author == request.user