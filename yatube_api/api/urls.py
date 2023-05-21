from django.urls import path
from djoser.views import ObtainAuthToken
from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

urlpatterns = [
    path('auth/token/', ObtainAuthToken.as_view(), name='token_obtain_pair'),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='post-detail'),
    path('groups/', GroupViewSet.as_view({'get': 'list'}), name='group-list'),
    path('groups/<int:pk>/', GroupViewSet.as_view({'get': 'retrieve'}), name='group-detail'),
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('posts/<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comment-detail'),
]
