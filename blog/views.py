from django.shortcuts import render
import sys
from .models import Post

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def map(request):
    return render(request, 'blog/map.html', {})

def index(request):
    return render(request, 'blog/index.html', {})

def test(request):
    return render(request, 'blog/jquery_ajax_1.html', {})




# Create your views here.
