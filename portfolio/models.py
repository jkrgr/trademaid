from django.db import models
from django.contrib.admin.models import User

class Player(User):
	name = models.CharField(max_length=50)
	phone_number = models.IntegerField()
	def __init__(self, *args, **kwargs):
		super(Player, self).__init__()
	def __init__(self, name, phone_number, email):
	    super(Player, self).__init__()
		base.email = email
		self.name = name
		self.phone_number = phone_number		

class Company(models.Model):
	ticker = models.CharField(max_length=30)
	name = models.CharField(max_length=255)
	openForTrade = models.BooleanField()
	def __init__(self, ticker, name, openForTrade):
		self.ticker=ticker
		self.name=name
		self.openForTrade = openForTrade

class CompanyStatistics(models.Model):
	id = models.AutoField(primary_key=True)
	ticker = models.ForeignKey(Company)
	p_e = models.DecimalField(max_digits=15, decimal_places=2)
	p_b = models.DecimalField(max_digits=15, decimal_places=2)
	ebitda = models.DecimalField(max_digits=15, decimal_places=2)
	recordDateTime = models.DateField(auto_now=True)
	def __init__(self, ticker, p_e, p_b, ebitda, recordDateTime):
		self.ticker=ticker
		self.p_e=p_e
		self.p_b=p_b
		self.ebitda=ebitda
		self.recordDateTime=recordDateTime

class CompanyAnalysis(models.Model):
	id=models.AutoField(primary_key=True)
	userID=models.ForeignKey(User)
	ticker=models.ForeignKey(Company)
	text=models.CharField(max_length=1000)
	bulls=models.IntegerField()
	def __init__(self, userID, ticker, text, bulls):
		self.userID=userID
		self.ticker=ticker
		self.text=text
		self.bulls=bulls
		
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