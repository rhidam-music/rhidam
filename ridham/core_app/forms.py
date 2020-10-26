from django import forms
from .models import Song
class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['songName', 'songLink']