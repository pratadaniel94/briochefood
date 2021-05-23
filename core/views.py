from django.shortcuts import render
from core.models import Product

# Create your views here.
def index(request):

    context = {
        "products": Product.objects.all()
    }
    return render(request, "index.html", context)

def get_product(request, id):

    context = {
        "product": Product.objects.get(id=int(id))
    }
    return render(request, "product.html", context)
