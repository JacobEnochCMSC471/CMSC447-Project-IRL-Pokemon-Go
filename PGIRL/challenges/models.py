from django.db import models

class Challenge(models.Model):
    required_level=models.IntegerField()
    required_experience=models.IntegerField()

