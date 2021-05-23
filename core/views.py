from django.shortcuts import render
from core.models import Product, Seller_Product

def index(request):

    context = {
        "products": Product.objects.all()
    }
    return render(request, "index.html", context)

def get_product(request):
    id_product = request.GET.get("product_id")
    context = {
        "product": Product.objects.get(id=id_product),
        "sellers": Seller_Product.objects.filter(id_product=id_product)
    }
    return render(request, "product.html", context)

def get_order(request):
    id_product = request.GET.get("product_id")
    id_seller = request.GET.get("seller_id")
    select_order = Seller_Product.objects.filter(id_product=id_product, id_seller=id_seller)
    context = {
        "seller": select_order[0],
        "range": range(1, select_order[0].amount+1)
    }
    return render(request, "order.html", context)
