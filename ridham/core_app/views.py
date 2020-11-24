from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from login_module.models import Profile
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm


from .forms import SongUploadForm, ProfileChangeForm, UserChangeForm
from .models import Song
import random
import string
import os
from mutagen.mp3 import MP3

@login_required
def user_profile(request):
    user = request.user
    profile = request.user.profile
    form1 = ProfileChangeForm(instance=profile)
    form2 = UserChangeForm(instance=user)
    form3 = PasswordChangeForm(user=request.user)
    context = {
        'form1' : form1,
        'form2' : form2,
        'form3' : form3, 
        'logged_in_user_username' : request.user,
    }
    
    if request.method == 'POST':
        form1 = ProfileChangeForm(request.POST, request.FILES, instance=profile)
        form2 = UserChangeForm(request.POST, request.FILES, instance=user)
        form3 = PasswordChangeForm(user=user, data=request.POST)

        if(form1.is_valid()):
            profile = form1.save()
            if(profile.profile_pic == ''):
                profile.profile_pic = 'noimage.jpg'
        if( form2.is_valid() ):
            user = form2.save()

        if(form3.is_valid()) : 
            form3.save()
            from django.core.mail import send_mail
            send_mail(
                'Your Password Has Been Changed',
                'Hello dear user, your password has been successfully updated.',
                'rhidam.helpdesk@gmail.com',
                [user.email],
                fail_silently=False,
            )
            
                

       


    return render(request, 'core_app/user_profile.html', context=context)

def HomepageView(request):
    return render(request, 'core_app/Homepage.html')
    pass

def generate_slug():
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(10))
    while len(Song.objects.filter(songSlug=result)) != 0:
        result = ''.join(random.choice(letters) for i in range(10))
    return result


@login_required
def dashboard(request):
    form = SongUploadForm()
    a = User.objects.filter(username=request.user)[0]
    user = Profile.objects.filter(user=a)[0]
    songs_list = Song.objects.filter(owner=user)
    
    context = {
        'form' : form,
        'songs_list' : songs_list,
        'my_user' : user.user,
    }

    if request.method == 'POST':
        songUploaded = request.POST['songup']
        if songUploaded == '1':
            form = SongUploadForm(request.POST, request.FILES)
            if form.is_valid():
                a = User.objects.filter(username=request.user)[0]
                user = Profile.objects.filter(user=a)[0]
                audio_data = request.FILES['songFile']
                print(audio_data)
                slug = generate_slug()
                audio_data.name = slug + '.mp3'
                new_song = Song(owner=user, songName=request.POST['songName'], songSlug=slug, songFile=audio_data)
                new_song.save()
            return redirect('core_app:dashboard')
    return render(request, 'core_app/dashboard.html', context=context)
            
