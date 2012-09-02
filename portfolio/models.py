from django.db import models
from django.contrib.admin.models import User

class Company(models.Model):
	ticker = models.CharField(max_length=30)
	name = models.CharField(max_length=255)
	openForTrade = models.BooleanField()
	def __init__(self, ticker, name, openForTrade):
		self.ticker=ticker
		self.name=name
		self.openForTrade = openForTrade


class StockQuote(models.Model):
	id = models.AutoField(primary_key=True)
	ticker = models.ForeignKey(Company)
	quote = models.DecimalField(max_digits=15, decimal_places=2)
	quotationDateTime = models.DateField(auto_now=True)
	def __init__(self, ticker, quote, quotationDateTime):
		self.ticker=ticker
		self.quote=quote
		self.quotationDateTime=quotationDateTime

class Trade(models.Model):
	id      = models.AutoField(primary_key=True)
	user    = models.ForeignKey(User)
	ticker  = models.ForeignKey(Company)
	quote_id   = models.ForeignKey(StockQuote)
	tradeDateTime = models.DateField(auto_now=True)
	volume = models.IntegerField()
	comment = models.TextField(blank=True)
	def __init__(self, user, ticker, quote_id, volume, comment):
		self.user = user
		self.ticker = ticker
		self.quote_id = quote_id
		self.volume = volume
		self.comment = comment