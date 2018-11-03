from django.db import models

class employee(models.Model):
    id = models.IntegerField(default=4,primary_key=True)
    name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=9,decimal_places=2)
    cno = models.IntegerField(default=10)
