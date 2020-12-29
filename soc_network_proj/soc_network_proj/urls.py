from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import UserCreateAPIView, UserRetrieveAPIView
from post.views import PostCreateAPIView, PostRetrieveAPIView, post_like, PostListAPIView


urlpatterns = [
    path('api/v1/accounts/create/', UserCreateAPIView.as_view()),
    path('api/v1/accounts/', UserRetrieveAPIView.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view()),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/post/create/', PostCreateAPIView.as_view()),
    path('api/v1/post/<int:pk>/', PostRetrieveAPIView.as_view()),
    path('api/v1/post/<int:pk>/like/', post_like),
    path('api/v1/posts/', PostListAPIView.as_view()),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [re_path(r'^.*', include('run.urls'))]
