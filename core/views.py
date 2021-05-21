from django.shortcuts import render
from core.models import Product

# Create your views here.
def index(request):

    context = {
        "products": Product.objects.filter(activate=True)
    }
    return render(request, "index.html", context)
