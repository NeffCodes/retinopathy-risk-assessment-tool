from django.shortcuts import render
from photos.models import RetinaPhoto

def homepage(request):
  photos = RetinaPhoto.objects.all()  
  context = {"photos":photos}

  return render(request, 'home.html', context)

def about(request):
  return render(request,'about.html')