from django.db import models
from django.utils import timezone


class Caffe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="No description yet)")
    photo = models.ImageField(upload_to='caffes')
    address = models.CharField(max_length=100)
    open_time = models.TimeField()
    close_time = models.TimeField()
    rating = models.FloatField(max_length=10)

    longtitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name} ({self.address})"


class Comment(models.Model):
    post = models.ForeignKey('Caffe', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    author_id = models.BigIntegerField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
