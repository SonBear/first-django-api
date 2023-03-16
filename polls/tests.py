from django.test import TestCase
from django.test import Client
from unittest.mock import patch
# Create your tests here.

class TestAlumnosAPI(TestCase):
    def setUp(self):
        self.client = Client()

    @patch("polls.views.index_students", autospec=True) # Create mock from view function
    def test_index_alumnos(self, mock_index_students):
        response = self.client.get('/sicei/alumnos')
        # Check if response is done and success
        self.assertEqual(response.status_code, 200)

        # Check if view is called
        self.assertEqual(mock_index_students.called, False)

