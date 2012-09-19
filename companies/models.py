from django.db import models
from django.contrib.admin.models import User


class Company(models.Model):
    """
    The companies of OBX
    """
    ticker = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    openForTrade = models.BooleanField()


class CompanyStatistics(models.Model):
    """
    Company statistics are regularly parsed from
    Bloomberg. KB has written the parser.
    """
    company = models.ForeignKey(Company)
    p_e     = models.DecimalField(max_digits=15, decimal_places=2)
    p_b     = models.DecimalField(max_digits=15, decimal_places=2)
    ebitda  = models.DecimalField(max_digits=15, decimal_places=2)
    recordDateTime = models.DateField(auto_now=True)


class CompanyAnalysis(models.Model):
    """
    User-uploaded analyses. Should support file uploading
    in the future.
    """
    userID  = models.ForeignKey(User)
    company = models.ForeignKey(Company)
    text    = models.CharField(max_length=1000)
    bulls   = models.IntegerField()


class StockQuote(models.Model):
    """
    The stock quotes
    """
    company = models.ForeignKey(Company)
    price   = models.DecimalField(max_digits=15, decimal_places=2)
    # When parsing the stocks, add correct date and time for last_trade
    last_trade = models.DateField(blank=False)
