# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase


class TestView(TestCase):

    def test_contact_create(self):
        """Test my article - uses 'django-templatepages'."""
        response = self.client.get('/article/my.html')
        self.assertEqual(200, response.status_code, 200)
        self.assertIn('Thank you', str(response.content))
