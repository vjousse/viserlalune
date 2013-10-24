# Create your views here.
from bestof.utils import render

from bestof.models import Category, Entry

def index(request):
    categories = Category.objects.all().order_by('sort')
    return render(request, 'bestof/index.html', {'categories': categories})
