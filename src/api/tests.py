from django.shortcuts import reverse

from rest_framework.test import APITestCase
from api.views import Category
from vlog.models import Category


class TestNoteApi(APITestCase):
    def setUp(self):
        # create category
        self.category = Category.objects.create(title="test")
        self.category.save()

    def test_category_creation(self):
        import ipdb
        ipdb.set_trace()

        response = self.client.get(reverse('category-list'))

        # assert new category was added
        self.assertEqual(Category.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    # def test_getting_categories(self):
    #     response = self.client.get(reverse('category-list'), format="json")
    #     self.assertEqual(len(response.data), 1)
    #
    # def test_updating_category(self):
    #     response = self.client.put(reverse('category-detail', kwargs={'slug': 'test'}), {  # kwargs={'pk': 1}
    #         'title': 'testing',
    #     }, format="json")
    #
    #     # check info returned has the update
    #     self.assertEqual('testing', response.data['title'])
    #
    # def test_deleting_category(self):
    #     response = self.client.delete(reverse('category-detail', kwargs={'slug': 'testing'}))  # kwargs={'pk': 1}
    #
    #     self.assertEqual(204, response.status_code)
