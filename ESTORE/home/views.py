from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from product.models import Product
from .models.orders import Order, Customer
from django.core.mail import send_mail
from django.views import View
from django.shortcuts import redirect,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from home.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from django.db.models import Sum

# Create your views here.

def index(request):
     
    data ={}
    categories = Category.objects.all()
    products = Product.objects.all()
    data['categories'] = categories
    data['products'] = products
    return render(request,'home/index.html',data)


# Signup
class signup(View):
    def get(self, request):
        return render(request,'home/signup.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password =postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register()
            return redirect ('index')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'home/signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
# login :
class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'home/login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        customer = Customer.get_customer_by_email (email)
        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('index')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'home/login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
#-----------------------------
def shop(request):
    
    data ={}
    #categories = list(Category.objects.values_list('CategoryName'))
    categories = Category.objects.all()
  
    if "Price00_100" in request.POST:
        products = Product.objects.filter(Price__gte=00, Price__lte=100)
    elif "Price100_200" in request.POST:
        products = Product.objects.filter(Price__gte=100, Price__lte=200)
    elif "Price200_300" in request.POST:
        products = Product.objects.filter(Price__gte=200, Price__lte=300)
    elif "Price300_400" in request.POST:
        products = Product.objects.filter(Price__gte=300, Price__lte=400)
    elif "Price400_500" in request.POST:
        products = Product.objects.filter(Price__gte=400, Price__lte=500)
    elif "ColorBlack" in request.POST:
        products = Product.objects.filter(Color__icontains ="black")
    elif "ColorWhite" in request.POST:
        products = Product.objects.filter(Color__icontains ="white")    
    elif "ColorBlue" in request.POST:
        products = Product.objects.filter(Color__icontains ="blue")    
    elif "ColorGreen" in request.POST:
        products = Product.objects.filter(Color__icontains ="green")
    elif "ColorRed" in request.POST:
        products = Product.objects.filter(Color__icontains ="red")      
    elif "SizeXL" in request.POST:
        products = Product.objects.filter(Size ="XL")      
    elif "SizeL" in request.POST:
        products = Product.objects.filter(Size ="L")   
    elif "SizeM" in request.POST:
        products = Product.objects.filter(Size ="M") 
    elif "SizeS" in request.POST:
        products = Product.objects.filter(Size ="S") 
    elif "SizeXS" in request.POST:
        products = Product.objects.filter(Size ="XS")     
    else: 
        products = Product.objects.all()

    data['categories'] = categories
    data['products'] = products
    return render(request,'home/shop.html',data)
   

def contact(request):
    if request.method == 'POST':
        Ho_Ten =request.POST["HoTen"]
        subject=request.POST['Subject']
        message =" from: " + request.POST['Email'] + '\n' + request.POST['Message'] # nhận diện email của khách hàng nào gửi 
        from_email='them.levan@mobifone.vn' 
        # from_email='thientri15102010@gmail.com'
        recipient_list=['levanthem2002@gmail.com',]
        send_mail(subject, message,from_email,recipient_list)
        return render(request, 'home/contact.html',{'Ho_Ten':Ho_Ten})
    else:
        return render(request,'home/contact.html',{})


class Cart1(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'home/cart1.html' , {'products' : products} )

class Cart(View):
    

    def post(self , request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else: 
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        print(product)
        return redirect('cart')

    def get(self , request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.objects.all()
        products = Product.objects.all()

        data = {}
        data['products'] = products
        data['categories'] = categories
        data['cart'] = cart

        print('you are : ', request.session.get('email'))
        return render(request, 'home/cart.html', data)

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.Price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('orders')
    

class OrderView(View):
    #   @method_decorator(auth_middleware) 
      def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        total_price =0
        for item in orders:
            total_price = total_price + item.product.Price * item.quantity
            
        request.session['totalPrice'] = total_price
       
        return render(request , 'home/orders.html'  , {'orders' : orders, 'total_price':total_price})
    

class Test(View):
    def post(self , request):
        product = request.POST.get('product')
        cart1 = request.session.get('cart1')
        remove = request.POST.get('remove')
      
        if cart1:
            
            quantity = cart1.get(product)
            print(quantity)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart1.pop(product)
                    else: 
                        cart1[product]  = quantity-1
                else:
                    cart1[product]  = quantity+1

            else:
                cart1[product] = 1
        else:
            cart1 = {}
            cart1[product] = 1

        request.session['cart1'] = cart1
        print('cart1' , request.session['cart1'])
        print(product)
        return redirect('test')

    def get(self,request):
        cart1 = request.session.get('cart1')
        if not cart1:
            request.session['cart1'] = {}
        return render(request,'home/test.html',{'cart1':cart1}) 

# thanh toan truc tuyen paypal
def payment(request):
    return render(request,'home/payment.html')

def paymentSuccess(request):
    
    return render(request,'home/paymentSuccess.html')
