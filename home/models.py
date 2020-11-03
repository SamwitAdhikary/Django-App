from django.db import models

# Create your models here.
class Conatct(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    content = models.TextField()

    def __str__(self):
        return 'Message From: ' + self.name