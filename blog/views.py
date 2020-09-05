from django.shortcuts import render
import requests
import sys
from .models import Post

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def map(request):
    return render(request, 'blog/map.html', {})





# Create your views here.
