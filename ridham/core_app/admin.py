from django.contrib import admin
from django.contrib.auth.models import User
from .models import Song

# Register your models here.
admin.site.register(Song)
