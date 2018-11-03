from django.db import models

class shop(models.Model):
    id=models.IntegerField(default=4,primary_key=True)
    name=models.CharField(max_length=50)
    salary=models.DecimalField(max_digits=10,decimal_places=2)

