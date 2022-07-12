
from django.urls import path,include

from . import views
from rest_framework import routers
from django.contrib import admin
from django.views.generic.base import TemplateView

router = routers.DefaultRouter()
router.register(r'order', views.OrderList)
router.register(r'user', views.UserList)
router.register(r'vendor', views.VendorList)
router.register(r'category', views.CategoryList)
router.register(r'customer', views.CustomerList)
router.register(r'product', views.ProductList)
router.register(r'superadmin', views.SuperAdminlist)
router.register(r'orderdetail', views.OrderDetail)





urlpatterns=[
 
    path('', include(router.urls)),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
 
]


