from django.db import models

# Create your models here.
Class UserStats(models.Model):
	user    = models.ForeignKey(User)
	balance = models.DecimalField(max_digits=15, decimal_places=2)
	#Fields to hold the change in net worth for different time periods
	change_day = models.DecimalField(max_digits=15, decimal_places=2)
	change_week = models.DecimalField(max_digits=15, decimal_places=2)
	change_month = models.DecimalField(max_digits=15, decimal_places=2)
	change_year = models.DecimalField(max_digits=15, decimal_places=2)
