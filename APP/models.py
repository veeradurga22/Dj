from contextlib import nullcontext
from email.policy import default
from django.db import models
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
# from store.models.customer import Customer
from django.views import View
import datetime 

# Create your models here.
class Category(models.Model):
	id=models.AutoField(primary_key=True)
	name = models.CharField(max_length=51)
	image = models.ImageField(upload_to='uploads\products',default=nullcontext)
	@staticmethod
	def get_all_categories():
		return Category.objects.all()
	def __str__(self):
		return self.name
	@staticmethod
	def get_all_categories_by_name(name):
		return Category.objects.filter(name=name)

class Product(models.Model):
    productname = models.CharField(max_length=200)
    MRP = models.IntegerField()
    discount = models.DecimalField(default = 0 ,max_digits=10, decimal_places=2)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    productfullname = models.TextField()
    description = models.TextField(default='')
    rating = models.DecimalField(default = 0,max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='uploads\products')
	

	# def __str__(self):
	# 	return super().__str__()
	
    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter (category=category_id)
        else:
            return Product.get_all_products()
	
	

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	address = models.TextField(max_length=100)
	pincode =  models.CharField(max_length=6)
	# to save the data
	def register(self):
		self.save()

	def __str__(self):
		return f"{self.first_name} {self.last_name} {self.email} {self.phone}"
	
	@staticmethod
	def get_customer_by_email(email):
		try:
			return Customer.objects.get(email=email)
		except:
			return False
	
	def isExists(self):
		if Customer.objects.filter(email=self.email):
			return True

		return False


class Order(models.Model):
	product = models.ForeignKey(Product,
								on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer,
								on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.IntegerField()
	address = models.CharField(max_length=100, default='', blank=True)
	phone = models.CharField(max_length=50, default='', blank=True)
	date = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)
	def placeOrder(self):
		self.save()
	@staticmethod
	def get_orders_by_customer(customer_id):
		return Order.objects.filter(customer=customer_id).order_by('-date')
	def __str__(self):
		return f"{self.product} {self.customer} {self.quantity} {self.price} "

GENDER_CHOICES = (
   ('S', 'Shipped'),
   ('O', 'OutofDelivery'),
   ('D','Delivered')

)
class Order_Item(models.Model):
	productids = models.CharField(max_length=200,default='', blank=True)
	customer = models.ForeignKey(Customer,
								on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.IntegerField()
	address = models.CharField(max_length=100, default='', blank=True)
	orderdate = models.DateField(default=datetime.datetime.today)
	deliverdate = models.DateField(default=datetime.datetime.today)
	size = models.CharField(max_length=5, default='', blank=True)
	status = models.CharField(default = '',choices=GENDER_CHOICES, max_length=128)

	def __str__(self):
		return f"{self.productids} {self.customer} {self.quantity} {self.price} {self.address}"

class Ordered_Product(models.Model):
	product = models.ForeignKey(Product,
								on_delete=models.CASCADE)
	orderitem = models.ForeignKey(Order_Item,
								on_delete=models.CASCADE)
	
	# def __str__(self):
	# 	return f"{self.product} {self.orderitem}"
	