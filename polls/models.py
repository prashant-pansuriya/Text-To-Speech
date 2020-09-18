from django.db import models

# Create your models here.
class Song(models.Model):

    song_file = models.FileField()

    def __str__(self):
        return str(self.id)
