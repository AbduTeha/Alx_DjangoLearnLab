from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        followed_users = self.request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        return posts