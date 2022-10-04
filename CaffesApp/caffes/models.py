from django.conf import settings
from django.db import models
from django.utils import timezone


class Caffe(models.Model):
    #long, lat
    name = models.CharField(max_length=100)
    description = models.TextField(default="No description yet)")
    photo = models.ImageField(upload_to='caffes')
    address = models.CharField(max_length=100)
    open_time = models.TimeField()
    close_time = models.TimeField()
    rating = models.FloatField(max_length=10)


    def __str__(self):
        return f"{self.name} ({self.address})"
