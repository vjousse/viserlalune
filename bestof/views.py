# Create your views here.
from bestof.utils import render

from bestof.models import Category, Entry

def index(request):
    categories = Category.objects.order_by('sort_index').all().select_related()
    print categories.query
    return render(request, 'bestof/index.html', {'categories': categories})
