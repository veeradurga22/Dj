from django.contrib import admin
from .models import *
class Customer_Title(admin.ModelAdmin):
  list_display = ("first_name", "last_name","email","phone")

class Order_Title(admin.ModelAdmin):
    list_display = ('product','customer','quantity','price')

class Order_Item_Title(admin.ModelAdmin):
    list_display = ('productids','customer','quantity','price','address')
  
# class Ordered_Product_Title(admin.ModelAdmin):
#   list_display = ('product','orderitem')
admin.site.register(Product)    
admin.site.register(Category)
admin.site.register(Customer,Customer_Title)
admin.site.register(Order,Order_Title)
admin.site.register(Order_Item,Order_Item_Title)
admin.site.register(Ordered_Product)

# admin.site.register(Login)




