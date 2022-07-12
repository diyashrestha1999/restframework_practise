from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Vendor(models.Model):
    owner = models.OneToOneField('auth.User', related_name='vendor', on_delete=models.CASCADE, default='')
    name=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
  

    
class Shop(models.Model):
    name=models.CharField(max_length=50)
    owner=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}, Owner: {self.owner} , Id: {self.id}"

class Category(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return f"Category: {self.name}"
      
class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name="category_name")
    shop=models.ManyToManyField(Shop, related_name="shop_name")
    
    @property
    def shop_detail(self):
        return list(self.shop.values_list("name","owner__name"))

    def __str__(self):
        return f"Product Name: {self.name}, shop: {self.shop}, category:{self.category}, id={self.id}"
    
class Customer(models.Model):
    owner = models.OneToOneField('auth.User', related_name='customer', on_delete=models.CASCADE, default='')
    name=models.CharField(max_length=100)
        
    def __str__(self):
        return f"{self.name}"


class SuperAdmin(models.Model):
    owner = models.OneToOneField('auth.User', related_name='super_admin', on_delete=models.CASCADE, default='')
    def __str__(self):
        return f"{self.owner.username}"

    
class Order(models.Model):
    order_date=models.DateField()
    pricing=models.FloatField()
    deliver_date=models.DateField()
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order ID:{self.id} Ordered Date:{self.order_date}, Pricing: {self.pricing}, Deliver Date: {self.deliver_date}, Ordered by:{self.customer}"
    
class OrderDetail(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Product Id: {self.product}, Order Id: {self.order}"
   