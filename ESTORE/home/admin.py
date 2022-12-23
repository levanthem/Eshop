from django.contrib import admin
from category.models import Category
from product.models import Product
from home.models.orders import Order
from home.models.customer import Customer
# Register your models here.
admin.site.register(Product) 
admin.site.register(Category) 
admin.site.register(Order)
admin.site.register(Customer)