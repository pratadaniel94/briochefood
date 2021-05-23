from django.shortcuts import render, HttpResponse
from core.models import Product, Seller_Product

def index(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, "index.html", context)

def search_product(product_id):
    try:
        return True, Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return False, HttpResponse("<h1>Produto não encontrado</h1>", status=404)

def valid_order(product_id, seller_id):
    try:
        order = Seller_Product.objects.filter(id_product=product_id, id_seller=seller_id)
        return True, order[0]
    except Exception:
        return False, HttpResponse("<h1>Pedido invalida</h1>", status=400)

def get_product(request):
    id_product = request.GET.get("product_id")
    product = search_product(id_product)
    if product[0]:
        context = {
            "product": product,
            "sellers": Seller_Product.objects.filter(id_product=id_product)
        }
        return render(request, "product.html", context)
    else:
        return product[1]

def get_order(request):
    id_product = request.GET.get("product_id")
    id_seller = request.GET.get("seller_id")
    select_order = valid_order(id_product, id_seller)
    if select_order[0]:
        context = {
            "seller": select_order[1],
            "range": range(1, select_order[1].amount+1)
        }
        return render(request, "order.html", context)
    else:
        return select_order[1]
