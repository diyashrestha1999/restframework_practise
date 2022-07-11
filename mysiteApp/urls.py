
from django.urls import path,include

from . import views
from rest_framework import routers
from django.contrib import admin
from django.views.generic.base import TemplateView

router = routers.DefaultRouter()
router.register(r'order-item', views.OrderList)



urlpatterns=[
    path('vendor/',views.VendorList.as_view(),name="vendor-list"),
    # path('addvendor/', views.post_index, name="addvendor"),
    path('vendor-detail/<int:pk>/',views.VendorDetail.as_view(),name='vednor-detail'),
    path('category/', views.CategoryList.as_view(),name="category"),
    path('category-detail/<int:id>',views.CategoryDetail.as_view(),name="category-list"),
    path('customer/',views.CustomerList.as_view(),name="customer-list"),
    path('customer-detail/<int:pk>',views.CustomerDetail.as_view(),name="customer-detail"),
    path('shop-list/',views.ShopList.as_view(),name='shop-list'),
    path('product-list/',views.ProductList.as_view(),name='product-list'),
    path('product-detail/<int:pk>',views.ProductDetail.as_view(),name='product-detail'),
    path('shop-detail/<int:pk>',views.ShopDetail.as_view(),name='shop-detail'),
    # path('order/',views.OrderList,name='order'),
    path('abc', views.CustomerList.as_view()),
    path('order/', include(router.urls)),


    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

# urlpatterns=format_suffix_patterns(urlpatterns)

