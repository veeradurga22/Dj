from http.client import HTTPResponse
from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import*
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages #import messages

from django.shortcuts import render
from .models import *
from django.views import View
from math import floor,trunc,ceil

def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    template = loader.get_template('index.html')
    if 'user' in request.session:
        current_user = request.session['user']
        customer = Customer.get_customer_by_email (current_user)
        context={
            'products':products,
            'categories':categories,
            'login':'login',
            'customer':customer,
            'home':1    
        }
    else:
        context={
            'products':products,
            'categories':categories, 
            'home':1 
        }
    # categories_filter = Category.objects.filter(products.name='Men')
    # return render(request, 'index.html', {'products':products,'categories':categories})
    return HttpResponse(template.render(context, request))

def Categories(request,id):
    products = Product.objects.filter(category_id=id)
    categories = Category.objects.all()
    template = loader.get_template('index.html') 
    if 'user' in request.session:
        current_user = request.session['user']
        customer = Customer.get_customer_by_email (current_user)
        context={
            'products':products,
            'categories':categories,
            'login':'login',
            'customer':customer    
        }
    else:
        context={
            'products':products,
            'categories':categories,  
        }
#   return HttpResponseRedirect(reverse('index'))
    # return redirect('index')
    return render(request,'index.html',context)

def Login(request):
    template = loader.get_template('login.html')

    return HttpResponse(template.render({}, request))
def Signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({}, request))
def Login_Page(request):
    # return render(request,'index.html')
    if request.method == 'POST':
        return_url = None
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        request.session['user'] = email
        customer = Customer.get_customer_by_email (email)
        error_message = None
        if customer:
            pswd = Customer.objects.filter(password=password)
            if pswd:
                products = Product.objects.all()
                categories = Category.objects.all()
                template = loader.get_template('index.html')
                idname = customer.id
                context={
                'products':products,
                'categories':categories,
                'login':'login',
                'idname':idname,
                'customer':customer
                }
                return HttpResponseRedirect(reverse('products'))
            else:
                error_message = 'Invalid password!!'
                return render (request, 'login.html', {'error': error_message})
        else:
            error_message = 'Invalid Customer Not Found !!'
            print (email, password)
            return render (request, 'login.html', {'error': error_message})
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render({}, request))
def Signup_Page(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    phone = request.POST['phone']
    address = request.POST['address']
    pin = request.POST['pin']
    data = Customer(first_name=firstname.upper(),last_name=lastname.upper(),phone=phone,email=email,password=password,address=address,pincode=pin)
    data.save()
    return render(request,'login.html')

def Logout(request):
    try:
        del request.session['user']
    except:
        return HttpResponseRedirect(reverse('Login'))
    return HttpResponseRedirect(reverse('products'))

def viewproduct(request):
    
    try:
        template = loader.get_template('product_details.html')
        p = request.POST['productid']
        product = Product.objects.get(id=p)
        current_user = request.session['user']
        customer = Customer.get_customer_by_email (current_user)
        return HttpResponse(template.render({'product':product,'customer':customer,'login':'login'},request))
    except:
        error_message = 'Login for product details'
        #print (email, password)
        return render (request, 'login.html', {'error': error_message})



def Addcart(request):
    # table1_rows = Product.objects.filter(id=id)
    # for row in table1_rows.values():
    #     Cart.objects.create(**row)
    products = Product.objects.all()
    categories = Category.objects.all()
    try:
        p = request.POST['productid']
        q = request.POST['quantity']
        # c = request.POST['customerid']
        
        current_user = request.session['user']
        customer = Customer.get_customer_by_email (current_user)
        pro = Product.objects.get(id=p)
        cus = Customer.objects.get(id=customer.id)
        ord_count = Order.objects.filter(product_id=p,customer_id=customer.id).count()

        if ord_count==0:
            data=Order(product=pro,customer=cus,quantity=int(q),price=pro.price,address=cus.address,phone=cus.phone,status='True')
            data.save()
        
    
        # template = loader.get_template('product_details.html')
        
        # product = Product.objects.get(id=p)
        # return HttpResponse(template.render({'product':product,'cart':1,'login':'login'},request))
        return HttpResponseRedirect(reverse('products'))        
    except Exception as e:
        error_message = 'Login for Add to Bag'
        #print (email, password)
        return render (request, 'login.html', {'error': e})
def Cart(request):
    template = loader.get_template('cart.html')
    current_user = request.session['user']
    customer = Customer.get_customer_by_email(current_user)
    data =  Order.objects.filter(customer_id = customer.id)
    products = Product.objects.all()
    count = data.count()
    # pro_price = Order.objects.filter(customer_id=customer.id).values('price')
    price = 0.0
    
    total = 0
    # dis_ord = Order.objects.filter(customer_id=customer.id).values('product_id')
    # dis=[]
    # for i in dis_ord:
    #     dis.append(Product.objects.filter(id=i['product_id']).values('discount')['discount'])
    # # for i in dis_ord:
    discount = 0.0
    for i in products:
        for j in data:
            if i.id==j.product_id:
                d = float(i.discount)
                price += float(i.MRP)
                discount += float(i.MRP)*d

    delivery_charges = 55
    total = round(price-discount+delivery_charges,2)
    
    t = str(total)
    ts= t.split('.')
    if int(ts[1])<6:
        total = floor(total)
    else:
        total = ceil(total)

    # total = ceil(total)
    discount = round(discount,2)
    context = {
        'orders':data,
        # 'customer':customer
        'products':products,
        'count':count,
        'price':price,
        'total':total,
        'discount':discount,
        'delivery':delivery_charges,
        'login':'login',
        'customer':customer,
    }
    return HttpResponse(template.render(context,request))
def Rm_item(request,id):
    current_user = request.session['user']
    cus = Customer.get_customer_by_email (current_user)
    member = Order.objects.get(product_id=id,customer_id = cus.id)

    member.delete()
    return HttpResponseRedirect(reverse('Cart'))



def address(request):
    template = loader.get_template('address.html')
    
    
    if request.method == 'POST':
        current_user = request.session['user']
        customer = Customer.get_customer_by_email(current_user)
        productid = request.POST['productid']
        quantity = request.POST['quantity']
        product = Product.objects.get(id=productid)
        discount = product.discount*product.MRP
        if product.price<500:
            delivery_charges = 55
        else:
            delivery_charges=0
        quantity = int(quantity)        
        MRP = product.MRP*quantity
        total = product.MRP-product.discount*product.MRP+delivery_charges
        t = str(total)
        ts= t.split('.')
        if int(ts[1])<6:
            total = floor(total)
        else:
            total = ceil(total)
        context = {
            'product':product,
            'count':quantity,
            'customer':customer,
            'discount':round(discount,0)*quantity,
            'delivery_charges':delivery_charges,
            'total':total*quantity,
            'MRP':MRP,
            'login':'login',
            'quantity':quantity,
            'address':1
        }
        return HttpResponse(template.render(context,request))
    else:
        current_user = request.session['user']
        customer = Customer.get_customer_by_email(current_user)
        orders = Order.objects.filter(customer_id= customer)
        quantity=0
        MRP=0
        discount = 0
        total = 0
        delivery_charges=55
        for order in orders:
            product = Product.objects.get(id=order.product_id)
            quantity += order.quantity
            MRP += product.MRP 
            discount += product.MRP*product.discount
            total += product.MRP-product.discount*product.MRP
        total += delivery_charges
        t = str(total)
        ts= t.split('.')
        if int(ts[1])<6:
            total = floor(total)
        else:
            total = ceil(total)
        context = {
            'product':product,
            'count':quantity,
            'customer':customer,
            'discount':round(discount,1),
            'delivery_charges':delivery_charges,
            'total':total,
            'MRP':MRP,
            'login':'login',
            'quantity':quantity,
            'address':1,
            'cart':1
        }
        return HttpResponse(template.render(context,request))

    
def profile(request):
    template = loader.get_template('profile.html')
    current_user = request.session['user']
    customer = Customer.get_customer_by_email(current_user)
    return HttpResponse(template.render({'customer':customer},request))

def summary(request):
    template = loader.get_template('order_summary.html')
    if request.method == 'POST':
        current_user = request.session['user']
        customer = Customer.get_customer_by_email(current_user)
        pid = request.POST['productid']
        quantity = request.POST['quantity']
        product = Product.objects.get(id=pid)
        discount = product.discount*product.MRP
        if product.price<500:
            delivery_charges = 55
        else:
            delivery_charges=0
        quantity = int(quantity)        
        MRP = product.MRP*quantity
        total = product.MRP-product.discount*product.MRP+delivery_charges
        t = str(total)
        ts= t.split('.')
        if int(ts[1])<6:
            total = floor(total)
        else:
            total = ceil(total)
        
        context = {
            'product':product,
            'count':quantity,
            'customer':customer,
            'discount':round(discount,0)*quantity,
            'delivery_charges':delivery_charges,
            'total':total*quantity,
            'MRP':MRP,
            'login':'login',
            'summary':1,
            'buy':1
        }
    else:
        current_user = request.session['user']
        customer = Customer.get_customer_by_email(current_user)
        orders = Order.objects.filter(customer_id= customer.id)
        products = Product.objects.all() 
        quantity=0
        MRP=0
        discount = 0
        total = 0
        delivery_charges=55
        for order in orders:
            product = Product.objects.get(id=order.product_id)
            quantity += order.quantity
            MRP += product.MRP 
            discount += product.MRP*product.discount
            total += product.MRP-product.discount*product.MRP
        total += delivery_charges
        t = str(total)
        ts= t.split('.')
        if int(ts[1])<6:
            total = floor(total)
        else:
            total = ceil(total)

        pids = ''
        for order in orders:
            pids+=str(order.product_id)+','
        
        context = {
            'count':quantity,
            'customer':customer,
            'discount':round(discount,1),
            'delivery_charges':delivery_charges,
            'total':total,
            'MRP':MRP,
            'login':'login',
            'quantity':quantity,
            'address':1,
            'orders':orders,
            'products':products,
            'cart':1,
            'summary':1
        }
    return HttpResponse(template.render(context,request))

def order(request):
    template = loader.get_template('order.html')
    if request.method == 'POST':
        current_user = request.session['user']
        customer = Customer.get_customer_by_email(current_user)
        pid = request.POST['productid']
        quantity = request.POST['quantity']
        product = Product.objects.get(id=pid)
        discount = product.discount*product.MRP
        if product.price<500:
            delivery_charges = 55
        else:
            delivery_charges=0
        quantity = int(quantity)        
        MRP = product.MRP*quantity
        total = product.MRP-product.discount*product.MRP+delivery_charges
        t = str(total)
        ts= t.split('.')
        if int(ts[1])<6:
            total = floor(total)
        else:
            total = ceil(total)
        orderitem = Order_Item(productids = pid,customer_id = customer.id,quantity = quantity,price = total*quantity,address = customer.address,size='M' )
        orderitem.save()
        orderedpoduct = Ordered_Product(product_id = pid,orderitem_id = orderitem.id)
        orderedpoduct.save()
       
    else:
        current_user = request.session['user']
        customer = Customer.get_customer_by_email(current_user)
        orders = Order.objects.filter(customer_id= customer.id)
        products = Product.objects.all() 
        quantity=0
        MRP=0
        discount = 0
        total = 0
        delivery_charges=55
        for order in orders:
            product = Product.objects.get(id=order.product_id)
            quantity += order.quantity
            MRP += product.MRP 
            discount += product.MRP*product.discount
            total += product.MRP-product.discount*product.MRP
        total += delivery_charges
        t = str(total)
        ts= t.split('.')
        if int(ts[1])<6:
            total = floor(total)
        else:
            total = ceil(total)

        pids = ''
        for order in orders:
            pids+=str(order.product_id)+','
        orderitem = Order_Item(productids = pids,customer_id = customer.id,quantity=quantity,price= total,address=customer.address)
        orderitem.save()
        for order in orders:
            orderproduct = Ordered_Product(product_id = order.product_id,orderitem_id = orderitem.id)
            orderproduct.save()
        
    return HttpResponse(template.render({'confirm':1},request))


def myorders(request):
    template = loader.get_template('orderspage.html')
    current_user = request.session['user']
    customer = Customer.get_customer_by_email(current_user)
    orders = Order_Item.objects.filter(customer_id=customer.id)
    ordered_product = Ordered_Product.objects.all()
    MRP = 0.0
    discount = 0.0
    total = 0.0
    delivery_charges = 0.0
    for order in orders:
        total += order.price
    for order in orders:
        for ordpro in ordered_product:
            if order.id == ordpro.orderitem_id:
                MRP += ordpro.product.MRP
                discount += float((ordpro.product.discount)*(ordpro.product.MRP))
                if ordpro.product.MRP<500:
                    delivery_charges += 55
                else:
                    delivery_charges=0
    context = {
        'orders':orders,
        'ordered_product':ordered_product,
        'customer':customer,
        'MRP':MRP,
        'discount':round(discount,1),
        'total':total,
        'delivery_charges':delivery_charges,
        'login':'login'
    }

    return HttpResponse(template.render(context,request))


def updateprofile(request):
    
    current_user = request.session['user']
    customer = Customer.get_customer_by_email(current_user)
    customer.first_name = request.POST['first_name']
    customer.last_name = request.POST['last_name']
    customer.email = request.POST['email']
    customer.password = request.POST['password']
    customer.phone = request.POST['phone']
    customer.address = request.POST['address']
    customer.pincode = request.POST['pincode']
    customer.save()
    template = loader.get_template('profile.html')
    customer = Customer.get_customer_by_email(current_user)
    return HttpResponse(template.render({'customer':customer},request))