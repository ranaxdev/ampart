from django.http import Http404, HttpResponse
from django.shortcuts import render

# Views
def index(request):
    return HttpResponse("Test");