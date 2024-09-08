from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2023
        }
        self.book = Book.objects.create(**self.book_data)
        self.url = '/api/books/'

    def test_create_book(self):
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, self.book_data['title'])

    def test_read_book(self):
        response = self.client.get(f'{self.url}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        update_data = {'title': 'Updated Title'}
        response = self.client.put(f'{self.url}{self.book.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, update_data['title'])

    def test_delete_book(self):
        response = self.client.delete(f'{self.url}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get(f'{self.url}?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        response = self.client.get(f'{self.url}?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_order_books(self):
        response = self.client.get(f'{self.url}?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], self.book.title)

    def test_authentication_required(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a user and generate a token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Initialize the API client
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
