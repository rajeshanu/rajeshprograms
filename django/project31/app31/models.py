from django.db import models
class register(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=10)

class login(models.Model):
    uemail=models.EmailField(primary_key=True)
    feedback=models.CharField(max_length=250)