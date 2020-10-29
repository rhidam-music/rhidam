from django import forms
from .models import Song
from login_module.models import Profile
from django.contrib.auth.models import User

class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['songName', 'songLink']