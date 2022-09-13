from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GropViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GropViewSet, basename='group')
router_v1.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
router_v1.register(r'follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    #базовые эндпоинты ('auth/users/', 'auth/users/me')
    path('v1/auth/', include('djoser.urls')),
    # эндпоинты для управлени JWT-токенами('auth/jwt/create/',
    # 'auth/jwt/refresh/)
    path('v1/auth/', include('djoser.urls.jwt')),
]
