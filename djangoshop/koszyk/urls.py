from django.urls import path
from . import views
urlpatterns=[
    path('koszyk/',views.show,name='koszyk'),
    path('add/<str:id>',views.add,name='add'),
    path('remove/<str:id>',views.remove,name='remove'),
    path('clean',views.clean,name='clean'),
    path('create_customer',views.create_customer,name='create_customer'),
    

]