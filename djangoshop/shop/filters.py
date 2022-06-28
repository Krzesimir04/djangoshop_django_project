import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
       super(ProductFilter, self).__init__(*args, **kwargs)
       self.filters['Name'].label="Szukaj"
    class Meta:
        model=Product
        fields=['Name']
   