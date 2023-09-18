from typing import Any
from django.db import models
class Doctor_Info(models.Model):
    doc_id = models.IntegerField(primary_key=True,max_length=5)
    doc_pass = models.TextField()
    doc_name = models.TextField(editable=True)
    doc_gender = models.CharField(choices=[('M','Male'),('F','Female')],max_length=1)
    doc_phn = models.IntegerField(max_length=10,unique=True)
    doc_area = models.TextField(editable=True)
    doc_hosp = models.TextField()
    def password(self):
        return self.doc_pass

class Doctor_Activity(models.Model):
    doc_id = models.ForeignKey(Doctor_Info,on_delete=models.CASCADE)
    doc_SI = models.DateTimeField()
    doc_SO = models.DateTimeField()
    doc_att = models.IntegerField()

