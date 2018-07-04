from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase


class CategoryTests(APITestCase):
    def test_create_category(self):
        url = reverse('category-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
