from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    #Id = models.AutoField(primary_key=True)
    ProductCode = models.CharField(max_length=100)
    Price = models.FloatField()
    Title = models.CharField(max_length=100)
    Size = models.CharField(max_length=100)
    Color =models.CharField(max_length=100)
    Description =models.CharField(max_length=100)
    Img1 = models.ImageField()
    Img2 = models.ImageField()
    Img3 = models.ImageField()
    Img4 = models.ImageField()
    Categoryid =models.ForeignKey(Category, on_delete=models.CASCADE)
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter (Categoryid=category_id)
        else:
            return Product.get_all_products();

    def __str__(self):
        return f"{self.ProductCode}  |  {self.Categoryid}"   # nhan dien qua name, thay vi object


       