from django.shortcuts import render
from product.models import Product
# Create your views here.

# Lay theo categoryId, nhieu product
def getProductByCategory(request,categoryId):
    lstProduct = Product.objects.filter(Categoryid=categoryId)
    data={}
    data['lstProduct']= lstProduct
    return render(request,'Product/listProduct.html',data)

# Lay theo productId, 1 product
def detailProduct(request,id):
    detailProduct = Product.objects.get(pk=id)
    return render(request,'Product/detailProduct.html',{'detailProduct':detailProduct})

def searchProduct(request):
    product_code = request.POST['LikePrdName']
    searchProduct = Product.objects.filter(ProductCode__icontains=product_code) 
    data={}
    data['searchProduct']= searchProduct
    return render(request,'product/listProductbyName.html',data)

# search product filter on link web
# def searchProduct(request,ProductCode):
    
#     searchProduct = Product.objects.filter(ProductCode__icontains=ProductCode) 
#     data={}
#     data['searchProduct']= searchProduct
#     return render(request,'product/listProductbyName.html',data)


def CountProductByCategory(request,categoryId):
    countProduct = Product.objects.filter(Categoryid=categoryId).count()
    data={}
    data['countProduct']= countProduct
    return render(request,'home/index.html',data)