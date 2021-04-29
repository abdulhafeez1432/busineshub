from django.urls import include, path
from .views import *

app_name = 'seller'

urlpatterns = [



    path("dashboard", SellerDashboard, name='seller-dashboard'),
    path("sellbusiness/", SellBusiness, name='sell-business'),
    path("addaboutbusiness/<pk>", AddAboutBusiness, name='about-business'),
    path("addstaffbusiness/<pk>", AddStaffBusiness, name='business-staff'),
    path("addfinancialbusiness/<pk>",
         AddFinancialBusiness, name='about-financial'),
    path("addtargetbusiness/<pk>", AddTargetBusiness, name='about-target'),
    path("addbusinesdocument/<pk>", AddBusinessDocument, name="busines-document"),
    path('contactus/', ContactUs, name='contact-us')








]
