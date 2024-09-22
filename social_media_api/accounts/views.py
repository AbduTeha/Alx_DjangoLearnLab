from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status
from .models import CustomUser



class RegisterView(APIView):
    def post(self, request):
        pass

class LoginView(APIView):
    def post(self, request):
        pass

class TokenView(APIView):
    def get(self, request):
        pass






class FollowView(APIView):
    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.get(id=user_id)
        request.user.following.add(user_to_follow)
        return Response(status=status.HTTP_201_CREATED)

class UnfollowView(APIView):
    def post(self, request, user_id):
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response(status=status.HTTP_200_OK)