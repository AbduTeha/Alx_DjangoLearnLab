from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, FeedView
from . import views
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view()),
    path('posts/<int:pk>/like/', views.LikeView.as_view()),
    path('posts/<int:pk>/unlike/', views.UnlikeView.as_view()),
]