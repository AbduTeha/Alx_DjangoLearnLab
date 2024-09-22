from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Post, Like
from .serializers import PostSerializer
from notifications.models import Notification

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


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            # Generate notification for post author
            notification = Notification(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            notification.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_200_OK)

class UnlikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        Like.objects.filter(post=post, user=request.user).delete()
        return Response(status=status.HTTP_200_OK)

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # Generate notification for post author
            notification = Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_200_OK)

class UnlikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return Response(status=status.HTTP_200_OK)