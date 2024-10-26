from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from products.models import ProductModel

def add_or_remove(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session['cart'] = cart

    return redirect(reverse_lazy('products:productlist'))


def get_user_cart(request):
    products = list()
    cart = request.session.get('cart', [])
    for product_id in cart:
        product_qs = ProductModel.objects.filter(pk=product_id)
        products.append(product_qs)

    return render(request, 'product-cart.html', context={'product': products})
