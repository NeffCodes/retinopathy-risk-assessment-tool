from django.http import HttpResponse

def homepage(request):
  return HttpResponse("Welcome Home")

def about(request):
  return HttpResponse("About this project")