from django.urls import path
from . import views

urlpatterns = [
     path('<int:categoryId>',views.getProductByCategory,name ='Danh sachs Product theo category id'),
     path('detail/<int:id>',views.detailProduct,name="Chi tiet Product"),
     # path('search/<str:ProductCode',views.searchProduct,name="searchProduct"),
     path('search/',views.searchProduct,name="searchProduct"),
     path('count/<int:categoryId>',views.CountProductByCategory,name="Count Product")
]
