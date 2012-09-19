from django.db import models
from django.contrib.admin.models import User


class Company(models.Model):
    ticker = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    openForTrade = models.BooleanField()


class CompanyStatistics(models.Model):
    id      = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company)
    p_e     = models.DecimalField(max_digits=15, decimal_places=2)
    p_b     = models.DecimalField(max_digits=15, decimal_places=2)
    ebitda  = models.DecimalField(max_digits=15, decimal_places=2)
    recordDateTime = models.DateField(auto_now=True)


class CompanyAnalysis(models.Model):
    id      = models.AutoField(primary_key=True)
    userID  = models.ForeignKey(User)
    company = models.ForeignKey(Company)
    text    = models.CharField(max_length=1000)
    bulls   = models.IntegerField()


class StockQuote(models.Model):
    id      = models.AutoField(primary_key=True)
    ticker  = models.ForeignKey(Company)
    quote   = models.DecimalField(max_digits=15, decimal_places=2)
    # When parsing the stocks, add correct date and time for last_trade
    last_trade = models.DateField(blank=False)
