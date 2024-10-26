from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db import models
from products import models


class ProductListView(ListView):
    template_name = 'product-list.html'
    model = models.ProductModel
    context_object_name = 'products'

    def get_queryset(self):
        return models.ProductModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.CategoryModel.objects.all()
        context['tags'] = models.TagModel.objects.all()
        context['colors'] = models.ColourModel.objects.all()
        context['brands'] = models.BrandModel.objects.all()
        return context


class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'


class ProductCartView(TemplateView):
    template_name = 'product-cart.html'


class ProductCheckoutView(TemplateView):
    template_name = 'product-checkout.html'
