from django.test import TestCase
from django.urls import resolve
from django.test import TestCase
from views import index
from django.http import HttpResponse, HttpRequest


# Create your tests here.

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
