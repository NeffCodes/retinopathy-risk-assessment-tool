from django.shortcuts import render
from photos.models import Photo

def homepage(request):
  photos = Photo.objects.all()  
  context = {"photos":photos}

  return render(request, 'home.html', context)

def about(request):
  return render(request,'about.html')