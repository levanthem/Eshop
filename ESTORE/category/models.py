from django.db import models

# Create your models here.

class Category(models.Model):
    Id = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100)
    CategoryCode = models.CharField(max_length=100)
    Parentid = models.IntegerField()
    image=models.ImageField(upload_to='image')
   

    def __str__(self):
        return f"{self.Id}  |  {self.CategoryName}  |   {self.CategoryCode} | {self.Parentid}"
        #return f"{self.CategoryName   # nhan dien qua name, thay vi object