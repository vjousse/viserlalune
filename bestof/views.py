# Create your views here.
from django.shortcuts import render

from bestof.models import Category, Entry

def index(request):
    context = {}
    return render(request, 'bestof/index.html', context)
