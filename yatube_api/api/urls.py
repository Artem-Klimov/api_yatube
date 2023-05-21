from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

from .views import (CommentViewSet, GroupViewSet,
                    PostViewSet, UserViewSet)

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', authtoken_views.obtain_auth_token),
    # path('api/v1/', include('djoser.urls.jwt')),
]
