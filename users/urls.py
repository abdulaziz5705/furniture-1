from django.urls import path
from .views import UserLogin, UserAccount, UserPassword, UserRegester, UserWishlist, NotFound

app_name = 'users'

urlpatterns = [
    path('userlogin/', UserLogin.as_view(), name='userlogin'),
    path('userregester/', UserRegester.as_view(), name='userregester'),
    path('useraccount/', UserAccount.as_view(), name='useraccount'),
    path('userpassword/', UserPassword.as_view(), name='userpassword'),
    path('userwishlist/', UserWishlist.as_view(), name='userwishlisy'),
    path('404/', NotFound.as_view(), name='404'),

]
