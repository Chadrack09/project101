from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=225)
    catchy = models.CharField(max_length=400)
    body = models.TextField()
    #thumbnail = models.ImageField(upload_to='')