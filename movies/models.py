from django.db import models

# Create your models here.


class Moviedata(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, default='action')
    duration = models.FloatField()
    rating = models.FloatField()
    image = models.ImageField(
        upload_to='Images/', default="Images/None/Noimg.jpg")

    def __str__(self):
        return self.name
