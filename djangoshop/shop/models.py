from django.db import models
from django.db.models import DecimalField, CharField, TextField, DateField,ImageField,ForeignKey
# Create your models here.

class Category(models.Model):
    Name=CharField(max_length=30,db_index=True,unique=True)

    def __str__(self):
        return self.Name

class Product(models.Model):
    Category=ForeignKey(Category,related_name='products',on_delete=models.CASCADE,default=1)
    Name=CharField(max_length=30)
    Description=TextField(max_length=300)
    Quantity=DecimalField(max_digits=5,decimal_places=0)
    Price=DecimalField(max_digits=7,decimal_places=2)
    Date=DateField(auto_now_add=True)
    Photo=ImageField(upload_to='photos/%Y/%m/%d',blank=True)

    class Meta:
        ordering=('Name',)
        index_together=(('id','Name'),)

    def __str__(self):
        x=self.Name
        return x


