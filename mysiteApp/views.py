
from unicodedata import category
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Vendor, Customer, Shop, Product,Order
from .serializers import CategorySerializer,UserSerializer, VendorSerializer, OrderDetailSerializer,CustomerSerializer,OrderSerializer,AdminSerializer,ShopSerializer,ProductSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# from mysiteApp.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from django.contrib.auth.models import User

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


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#using generic class based view
class VendorList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

    def create(self, request, *args, **kwargs):
        if not request.user.username in Vendor.objects.all().values_list('username', flat=True):
            self.permission_denied(request, message="permission nai xaina.")
        
        return super().create(request, *args, **kwargs)


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

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

class CategoryList(APIView):
    def get(self,request,format=None):
        categories=Category.objects.all()
        ser=CategorySerializer(categories,many=True)
        return Response(ser.data)
    def post(self,request,format=None):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

# using APIView
class CategoryDetail(APIView):
    def get(self,request,id,format=None):
        category=Category.objects.get(pk=id)
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    def patch(self,request,id,format=None):
        category=Category.objects.get(pk=id)
        serializer=CategorySerializer(category,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    def delete(self,request,id,format=None):
        Category.objects.get(pk=id).delete()
        return Response("Deleted")

# using mixins
class CustomerList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# using mixins
class CustomerDetail(
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
  
    def get(self, request, pk, **kwargs):
  
        return self.retrieve(request, pk, **kwargs)

    def put(self, request, pk, **kwargs):
 
        return self.update(request, pk, **kwargs)

    def delete(self, request, pk, **kwargs):
        
        return self.destroy(request, pk, **kwargs)

class ShopList(generics.ListCreateAPIView):
    queryset=Shop.objects.all()
    serializer_class=ShopSerializer

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Shop.objects.all()
    serializer_class=ShopSerializer

class ProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class AdminList(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=AdminSerializer

class OrderList(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer


