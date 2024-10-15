from django.shortcuts import render
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'contact.html'


class AboutView(TemplateView):
    template_name = 'about-us.html'


class BlogDetailView(TemplateView):
    template_name = 'blog-detail.html'


class BlogListView(TemplateView):
    template_name = 'blog-list.html'


class HomeView(TemplateView):
    template_name = 'home.html'
