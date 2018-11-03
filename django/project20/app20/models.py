from django.db import models

class course(models.Model):
    id=models.IntegerField(default=2,primary_key=True)
    name=models.CharField(max_length=50)
    duration=models.IntegerField(default=4)
    fee=models.IntegerField(default=5)
class faculity(models.Model):
    id = models.IntegerField(default=2, primary_key=True)
    name = models.CharField(max_length=50)
    cname = models.CharField(max_length=50)
    cno=models.IntegerField(default=10)
    experiance=models.DecimalField(max_digits=2,decimal_places=1)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
class newclass(models.Model):
    id = models.IntegerField(default=2, primary_key=True)
    name = models.CharField(max_length=50)
    time=models.TimeField()
    date=models.DateField()