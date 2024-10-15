from django.shortcuts import render
from django.views.generic import TemplateView


class UserAccount(TemplateView):
    template_name = 'user-acount.html'


class UserLogin(TemplateView):
    template_name = 'user-login.html'


class UserRegester(TemplateView):
    template_name = 'user-register.html'


class UserPassword(TemplateView):
    template_name = 'user-reset-password.html'


class UserWishlist(TemplateView):
    template_name = 'user-wishlist.html'


class NotFound(TemplateView):
    template_name = '404.html'