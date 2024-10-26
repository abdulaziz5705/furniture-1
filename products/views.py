
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from products.models import ProductModel


class ProductListView(ListView):
    template_name = 'product-list.html'
    model = ProductModel
    context_object_name = 'products'


class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'


class ProductCartView(TemplateView):
    template_name = 'product-cart.html'


class ProductCheckoutView(TemplateView):
    template_name = 'product-checkout.html'

