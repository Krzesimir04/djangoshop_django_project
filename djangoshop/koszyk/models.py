from django.db import models
from shop.models import Product
# Create your models here.
Oczekiwanie_na_płatność='Oczekiwanie na płatność'
Realizacja='Realizacja'
W_drodze='W drodze'
Dostarczono='Dostarczono'
STATUS=[(Oczekiwanie_na_płatność,'Oczekiwanie na płatność'),(Realizacja,'Realizacja'),(W_drodze,'W drodze'),(Dostarczono,"dostarczono"),]

class Customer(models.Model):
    Name=models.CharField(max_length=20)
    Surname=models.CharField(max_length=20)
    Address=models.CharField(max_length=90)
    Email=models.EmailField(max_length=80)
    Tel=models.IntegerField()
    def __str__(self):
        return str(self.id)+', '+self.Name

class Order(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    QunatityOfProduct=models.IntegerField(null=True)
    Price=models.FloatField(null=True)
    Date=models.DateTimeField(auto_now_add=True)
    Status=models.CharField(choices=STATUS, max_length=30,default=Oczekiwanie_na_płatność)
    def __str__(self):
        return 'Produkt: '+self.product.Name+', kupujący: '+str(self.customer)+', Adres: '+self.customer.Address
