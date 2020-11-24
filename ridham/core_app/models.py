from django.db import models
from login_module.models import Profile

class Song(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    songName = models.CharField(max_length=64)
    songFile = models.FileField()
    songSlug = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.songName
