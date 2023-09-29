from django.test import TestCase
from rest_framework.status import HTTP_200_OK
from django.urls import reverse
from .views import PublicApiView


class TestPublicApiView(TestCase):
    # Returns a response with a timestamp when GET request is made
    def test_get_request_returns_timestamp(self):
        response = PublicApiView().get(None)
        self.assertIn("ts", response.data)
        self.assertIsInstance(response.data["ts"], float)

class PublicApiViewTests(TestCase):
    # Returns a response with a timestamp when GET request is made
    def test_get_request_returns_timestamp(self):
        response = self.client.get(reverse("unix_api"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIsInstance(response.data["ts"], float)