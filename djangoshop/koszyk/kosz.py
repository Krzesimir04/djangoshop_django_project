from shop.models import Product
from decimal import Decimal
class Koszyk():
    def __init__(self,request):
        koszyk=request.session.get('produkty')
        if not koszyk:
            koszyk=request.session['produkty']={}
        self.koszyk=koszyk
        self.koszykLength=len(self.koszyk.values())

    def __iter__(self):
        products_ids=self.koszyk.keys()
        products=Product.objects.filter(id__in=products_ids)
        koszyk=self.koszyk.copy()
        for product in products:
            koszyk[str(product.id)]['product']=product
        for item in self.koszyk.values():
            item['product']=item['product']
            item['quantity']=int(item['quantity'])
            item['price']=float(item['price'])
            item['totalprice']=item['price']*item['quantity']
            yield item
            

    def add(self,object,request,quantity=1):
        productadd_id=str(object.id)
        if productadd_id in self.koszyk:
            x=int(self.koszyk[str(object.id)]['quantity'])
            x+=int(quantity)
            self.koszyk[str(object.id)]['quantity']=str(x)
        else:
            self.koszyk[str(object.id)]={'quantity':str(quantity),'price':str(object.Price)}
        request.session.modified=True

    def remove(self,object_id,request):
        del self.koszyk[str(object_id)]
        request.session.modified=True

    def clear(self,request):
        request.session.clear()

    