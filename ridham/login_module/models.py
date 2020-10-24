from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=32)
    passWord = models.CharField(max_length=32)
    emailId = models.CharField(max_length=64)
    isBlocked = models.BooleanField()
    def __str__(self) -> str:
        return self.userName
    def get_song_list(self):
        return Song.objects.filter(owner = self)
    

class Song(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    songName = models.CharField(max_length=64)
    songLink = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.songName

class LoginHistory(models.Model):
    loginTime = models.DateTimeField()
    userName = models.CharField(max_length=32)
    loginIp = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.userName


