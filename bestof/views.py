# Create your views here.
from bestof.utils import render

from bestof.models import Category, Entry

def index(request):
    return render(request, 'bestof/index.html')
