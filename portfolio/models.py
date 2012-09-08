from django.db import models
from core.models import User
from companies.models import StockQuote, Company


class CompanyStatistics(models.Model):
	id = models.AutoField(primary_key=True)
	ticker = models.ForeignKey(Company)
	p_e = models.DecimalField(max_digits=15, decimal_places=2)
	p_b = models.DecimalField(max_digits=15, decimal_places=2)
	ebitda = models.DecimalField(max_digits=15, decimal_places=2)
	recordDateTime = models.DateField(auto_now=True)


class Trade(models.Model):
	id      = models.AutoField(primary_key=True)
	user    = models.ForeignKey(User)
	ticker  = models.ForeignKey(Company)
	quote_id   = models.ForeignKey(StockQuote)
	tradeDateTime = models.DateField(auto_now=True)
	volume = models.IntegerField()
	comment = models.TextField(blank=True)
