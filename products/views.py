
from django.shortcuts import render
from django.views.generic import TemplateView


class ProductListView(TemplateView):
    template_name = 'product-list.html'


class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'


class ProductCartView(TemplateView):
    template_name = 'product-cart.html'


class ProductCheckoutView(TemplateView):
    template_name = 'product-checkout.html'

