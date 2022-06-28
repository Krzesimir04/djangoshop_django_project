from cProfile import label
from inspect import modulesbyfile
from django.shortcuts import render
from .models import Product,Category
from koszyk.forms import AddProduct
from .filters import ProductFilter
# Create your views here.


def base(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    myFilter=ProductFilter(request.GET, queryset=products)
    products=myFilter.qs
    return render(request, 'base.html',{'products':products,'categories':categories,'myFilter':myFilter})

def filtr(request,name):
    categories=Category.objects.all()
    nameCat=Category.objects.get(Name=name)
    products=Product.objects.filter(Category=nameCat)
    myFilter=ProductFilter(request.GET, queryset=products)
    return render(request,'base.html',{'name':name,'products':products,'categories':categories,'myFilter':myFilter})

def product(request,pk):
    product=Product.objects.filter(id=pk)
    categories=Category.objects.all()
    addProductForm=AddProduct()
    myFilter=ProductFilter(request.GET)
    return render(request, "product.html",{'categories':categories,'pk':pk,'product':product,'AddProductForm':addProductForm,'myFilter':myFilter})



def kontakt(request):
    categories=Category.objects.all()
    myFilter=ProductFilter(request.GET)
    return render(request,'kontakt.html',{'categories':categories,'myFilter':myFilter})

def o_nas(request):
    categories=Category.objects.all()
    myFilter=ProductFilter(request.GET)
    return render(request,'o_nas.html',{'categories':categories,'myFilter':myFilter})