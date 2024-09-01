# api/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book_list'),
    path('', include(router.urls)),
]
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='books')


    