
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Vendor, Customer, Shop, Product,Order,SuperAdmin
from .serializers import CategorySerializer,UserSerializer, OrderDetail,VendorSerializer, OrderDetailSerializer,CustomerSerializer,OrderSerializer,AdminSerializer,ShopSerializer,ProductSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from mysiteApp.permissions import SuperUserPermission
from rest_framework import permissions
from django.contrib.auth.models import User



class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



#using generic class based view
class VendorList(viewsets.ModelViewSet):

    permission_classes = [SuperUserPermission]
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

    # def create(self, request, *args, **kwargs):
    #     if request.data.get('owner') != request.user.id:
    #         return self.permission_denied(request, message="bigriyoooooooo")
    #     return super().create(request, *args, **kwargs)



class CategoryList(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class CustomerList(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
  
class ShopList(viewsets.ModelViewSet):
    queryset=Shop.objects.all()
    serializer_class=ShopSerializer


class ProductList(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class SuperAdminlist(viewsets.ModelViewSet):
    queryset=SuperAdmin.objects.all()
    serializer_class=AdminSerializer


class OrderList(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderDetail(viewsets.ModelViewSet):
    queryset=OrderDetail.objects.all()
    serializer_class=OrderDetailSerializer



# using functions
# @api_view(['GET','POST'])
# def get_index(request):
#     if request.method=='GET':
   
#         vendors = Vendor.objects.all()
#         serializer=VendorSerializer(vendors, many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=VendorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

# class CustomPermission(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # # so we'll always allow GET, HEAD or OPTIONS requests.
#         print('safe methods', permissions.SAFE_METHODS)

#         if request.method in permissions.SAFE_METHODS:
#             return False
        

#         return False
#         # Write permissions are only allowed to the owner of the snippet.
#     def has_permission(self, request, view):
#         return True


# @api_view(['Get','PUT','DELETE','PATCH'])
# def vendor_detail(request, id):
#     if request.method=='GET':
#         vendors= Vendor.objects.get(pk=id)
#         serializer=VendorSerializer(vendors)
#         return Response(serializer.data)

#     elif request.method=='PUT':
#         vendors= Vendor.objects.get(pk=id)
#         serializer=VendorSerializer(vendors,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     elif request.method=='PATCH':
#         vendors= Vendor.objects.get(pk=id)
#         serializer=VendorSerializer(vendors,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     elif request.method=='DELETE':
#         Vendor.objects.get(pk=id).delete()
#         return Response("no data to display")