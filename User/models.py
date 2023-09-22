from django.db import models
class User_Info(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    phone = models.BigIntegerField(primary_key=True)
    address = models.TextField()
    gender = models.CharField(choices=[('M','Male'),('F','Female')],max_length=1)



