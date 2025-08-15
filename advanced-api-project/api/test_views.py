from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user and login
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create a sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            published_year=2024
        )

       #urls
        self.list_url = reverse('list_books')
        self.detail_url = reverse('retrieve_book', kwargs={'pk': self.book.pk})
        self.create_url = reverse('create_book')
        self.update_url = reverse('update_book', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('delete_book', kwargs={'pk': self.book.pk})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data[0])  # Using response.data

    def test_get_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)  # Using response.data

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "published_year": 2025
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])  # Using response.data

    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "published_year": 2026
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")  # Using response.data

    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
