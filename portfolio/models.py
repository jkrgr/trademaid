from django.db import models
from django.contrib.admin.models import User


class Trade(models.Model):
    id      = models.AutoField(primary_key=True)
    ticker  = models.CharField(max_length=255)
    price   = models.DecimalField(max_digits=15, decimal_places=2)
    buy     = models.BooleanField(default=True)
    comment = models.TextField(blank=True)
    user    = models.ForeignKey(User)

    def __init__(self, ticker, price, buy, comment, user):
        self.ticker = ticker
        self.price = price
        self.buy = buy
        self.comment = comment
        self.user = user