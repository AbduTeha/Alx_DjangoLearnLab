# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
        }

    def test_create_book(self):
        response = self.client.post(reverse('book-list'), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, self.book_data['title'])

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        updated_data = {'title': 'Updated Title'}
        response = self.client.put(reverse('book-detail', args=[book.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get().title, updated_data['title'])

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.delete(reverse('book-detail', args=[book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_authentication_required(self):
        # Test that authentication is required for CRUD operations
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_permission_required(self):
        # Test that permission is required for CRUD operations
        response = self.client.post(reverse('book-list'), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)