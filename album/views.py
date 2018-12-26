from django.shortcuts import render, redirect,get_object_or_404
from rooms.models import Room
from .models import Photo
from .forms import PhotoForm
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required    
def photo_delete(request):
    photo = get_object_or_404(Photo,pk=pk)
    room = get_object_or_404(Room,pk=room_pk)
    photo.delete()
    template_name = 'album/photo_delete.html'
    success_url = reverse_lazy('photo_list')




def photo_list(request,pk):#pk of the respesctive Room
    room = get_object_or_404(Room,pk=pk)
    photos = Photo.objects.filter(room=room)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            if room.images.count() < 5:
                try:
                    photo = form.save()
                    photo.room = room
                    print(photo.room)
                    photo.save()
                except:
                    print('failed to create file')
                
                
                messages.info(request,'Photo upload Successful!')
            else:
                messages.error(request,'You have exceeded the upload limit!')
            return redirect('photo_list',pk)
    else:
        form = PhotoForm()
    return render(request, 'album/photo_list.html', {'form': form, 'photos': photos,'room':room})