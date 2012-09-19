"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Company

class CompanyTest(TestCase):
    def test_find_company(self):
        """ Try to find some common stocks in the DB
        """


