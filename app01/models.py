from django.db import models

class UserMessage(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    age = models.CharField(max_length=3)
    message = models.TextField()
