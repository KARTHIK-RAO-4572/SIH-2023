from django.db import models

class Asha_Info(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    phone = models.BigIntegerField(primary_key=True)
    village = models.TextField()
    password = models.TextField()
