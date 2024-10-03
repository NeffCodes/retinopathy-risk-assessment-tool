from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from cloudinary.forms import cl_init_js_callbacks      
from .models import Photo
from .forms import PhotoForm

def upload(request):
    context = dict( backend_form = PhotoForm())

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'upload.html', context)