from models import Product
from . import forms
from category.models import Category
from django.db import models

class ProductForm(forms.Form):
    
    Id = forms.AutoField(primary_key=True)
    ProductCode = forms.CharField(max_length=100)
    Price = forms.FloatField()
    Title = forms.CharField(max_length=100)
    Size = forms.CharField(max_length=100)
    Color =forms.CharField(max_length=100)
    Description =forms.CharField(max_length=100)
    Img1 = forms.ImageField()
    Img2 = forms.ImageField()
    Img3 = forms.ImageField()
    Img4 = forms.ImageField()
    Categoryid =forms.models.ForeignKey(Category, on_delete=models.CASCADE)