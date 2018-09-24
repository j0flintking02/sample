from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from .models import Entries
from .views import EntriesView


class EntriesTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.entries = Entries.objects.create(title="some new title", description="lorem ipsum")

    def test_get(self):
        request = self.factory.get('/Entries/')
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        view = EntriesView.as_view({'post': 'list'})
        
        # Generating the request
        request = self.factory.post('/Entires/', {'title': 'some new title', 'description': 'lorem ipsum'},format='json')
        
        response = view(request)
        expected = {'title': self.entries.title, 'description': self.entries.description}
        
        self.assertEqual(response.status_code, 201)  # 201 = created
        self.assertEqual(response.data, expected)