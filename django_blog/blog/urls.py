from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:post_pk>/comments/', views.CommentListView.as_view(), name='comment_list'),
    path('posts/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('posts/<int:post_pk>/comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('posts/<int:post_pk>/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('posts/<int:post_pk>/comments/', views.CommentListView.as_view(), name='comment_list'),
    path('posts/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]