from django.urls import path
from orders.views import add_or_remove, get_user_cart
app_name = 'orders'

urlpatterns = [
    path('card/<int:pk>/', add_or_remove, name='add-or-remove'),
    path('card/', get_user_cart, name='cart'),

]