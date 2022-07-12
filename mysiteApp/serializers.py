from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Order, Product, Shop, Vendor, Customer,SuperAdmin,OrderDetail

class UserSerializer(serializers.ModelSerializer):
    # vendors = serializers.PrimaryKeyRelatedField(many=True, queryset=Vendor.objects.all())
    class Meta:
        model=User
        fields=['username','email']

class VendorSerializer(serializers.ModelSerializer):
    shop_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Shop.objects.all())
    class Meta:
        model= Vendor
        fields='__all__'


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields='__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'


class ShopSerializer(serializers.ModelSerializer):
    # vendor_set=serializers.PrimaryKeyRelatedField(many=True, queryset=Vendor.objects.all())
    class Meta:
        model=Shop
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=SuperAdmin
        fields='__all__' 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDetail
        fields='__all__'