from django.db import models

# Create your models here.


class PubgTournaments(models.Model):
    type = models.CharField(max_length=200)
    map = models.CharField(max_length=200)
    entryFees = models.CharField(max_length=200)
    time = models.DateTimeField("date published")
    payMode = models.CharField(max_length=200)
    furtherInfo = models.CharField(max_length=1000)

