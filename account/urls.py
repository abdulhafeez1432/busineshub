from django.urls import include, path
from .views import * 


app_name = 'acount'

urlpatterns = [
   
    path('', home, name='index'),
    path('logout', logout_user, name='user-logout'),
    path("login", login, name='user-login'),
    path('buyersignup/', BuyerSignUpView.as_view(), name='buyer-signup'),
    path('sellersignup/', SellerSignUpView.as_view(), name='seller-signup'),

    
 

   
]