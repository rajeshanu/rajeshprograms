from django.db import models
class Feedback(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10)
    feedback=models.CharField(max_length=200)
