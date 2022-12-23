from .models import Category
from . import forms

class Category(forms.Form):
    Id = forms.AutoField(primary_key=True)
    CategoryName = forms.CharField(max_length=100)
    CategoryCode = forms.CharField(max_length=100)
    Parentid =forms.IntegerField()
    image=forms.ImageField(upload_to='image')