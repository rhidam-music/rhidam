from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isBlocked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username
    def get_song_list(self):
        return Song.objects.filter(owner = self)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Song(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
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

class Forgot(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(blank=False)

