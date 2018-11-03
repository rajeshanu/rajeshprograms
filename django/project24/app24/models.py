from django.db import models
class profile(models.Model):
    no=models.IntegerField(default=4,primary_key=True)
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10)
    path=models.CharField(max_length=50)
# Create your models here.
