from django.urls import path
from .views import ContactView, AboutView, BlogDetailView, BlogListView, HomeView

app_name = "pages"


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about_us/', AboutView.as_view(), name='about'),
    path('blogdetail/', BlogDetailView.as_view(), name='blog-detail'),
    path('bloglist/', BlogListView.as_view(), name='blog-list'),

]
