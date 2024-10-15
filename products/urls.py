from django.urls import path
from .views import ProductCartView, ProductListView, ProductDetailView, ProductCheckoutView

app_name = 'product'

urlpatterns = [
    path('productcard/', ProductCartView.as_view(), name='productcard'),
    path('productlist/', ProductListView.as_view(), name='productlist'),
    path('productdetail/', ProductDetailView.as_view(), name='productdetail'),
    path('productcheckout/', ProductCheckoutView.as_view(), name='productcheckout'),

]