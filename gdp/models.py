from django.db import models

# Create your models here.
class Gdp(models.Model):
    year = models.IntegerField()
    gdp_usd_billion = models.FloatField()
