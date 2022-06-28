from itertools import product
from django.shortcuts import redirect, render
from .kosz import Koszyk
from .forms import *
from shop.models import Product
from .tasks import customer_created
# Create your views here.

def add(request,id):
    if request.method=='POST':
        AddProductForm=AddProduct(request.POST)
        if AddProductForm.is_valid():
            ProductToAdd=Product.objects.filter(id=id)
            quantity=request.POST['quantity']
            koszyk=Koszyk(request)
            for data in ProductToAdd:
                koszyk.add(data,request,quantity)
            return redirect('/koszyk/koszyk')
        else:
            return redirect('')

    else:
        return redirect('')

def show(request):
    koszyk=Koszyk(request)
    status=0
    totalPrice=0
    for item in koszyk:
        totalPrice+=float(item['price'])*int(item['quantity'])
        print(totalPrice)
        if item['quantity'] > item['product'].Quantity:
            status=1
    if request.session['produkty']=={}:
        status=2
    return render(request,'koszyk.html',{'koszyk':koszyk,'status':status,'totalPrice':totalPrice})

def clean(request):
    kosz=Koszyk(request)
    kosz.clear(request)
    return redirect('/koszyk/koszyk')

def remove(request,id):
    koszyk=Koszyk(request)
    koszyk.remove(id,request)
    return redirect('/koszyk/koszyk')


def create_customer(request):
    form=CustomerForm()
    koszyk=Koszyk(request)
    totalPrice=0
    for item in koszyk:
        totalPrice+=float(item['price'])*int(item['quantity'])
    if request.method=='POST':
            form=CustomerForm(request.POST)
            if form.is_valid():
                customer=form.save()
                for item in koszyk:
                    Order.objects.create(customer=customer,product=item['product'],QunatityOfProduct=item['quantity'],Price=item['price'],)
                    product=Product.objects.get(id=item['product'].id)
                    product.Quantity=product.Quantity-item['quantity']
                    product.save()
                koszyk.clear(request)
                #customer_created.delay(customer.id)

                return render(request,'potwierdzenie.html',{'order':customer})

    return render(request,'create_customer.html',{'form':form,'koszyk':koszyk,'totalPrice':totalPrice})
