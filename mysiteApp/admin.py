from django.contrib import admin
from .models import Category, Customer, OrderDetail, Product, Vendor, Shop, Order,SuperAdmin
# Register your models here.
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(SuperAdmin)
admin.site.register(Category)