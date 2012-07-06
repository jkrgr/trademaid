"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.admin.models import User
from portfolio.models import Trade

class PortfolioTest(TestCase):
    #fixtures = ['portfolio_testdata.json']

    def test_index(self):
        resp = self.client.get('/portfolio/')
        self.assertEqual(resp.status_code, 200)

    def test_make_trade(self):
        """
        Let a User make a Trade
        """
        u = User.objects.all()[0]
        t = Trade(ticker = 'HLNG', price = '51.20', buy = True, comment = 'Test', user=u)
        self.assertEqual(t.ticker, 'HLNG')
        self.assertEqual(t.price, '51.20')
