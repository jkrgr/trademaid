from django.db import models
from core.models import User
from companies.models import StockQuote, Company



class Trade(models.Model):
	id      = models.AutoField(primary_key=True)
	user    = models.ForeignKey(User)
	ticker  = models.ForeignKey(Company)
	quote_id   = models.ForeignKey(StockQuote)
	tradeDateTime = models.DateField(auto_now=True)
	volume = models.IntegerField()
	comment = models.TextField(blank=True)
