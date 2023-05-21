from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from djoser.views import TokenCreateView, UserViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    # path('api/v1/api-token-auth/', TokenCreateView.as_view(), name='token_create'),
    # path('api/v1/users/', UserViewSet.as_view({'post': 'create'}), name='user_create'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
