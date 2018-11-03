from django.db import models

class shop(models.Model):
    id=models.IntegerField(default=2,primary_key=True)
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=9,decimal_places=2)
    quntity= models.IntegerField(default=2)
