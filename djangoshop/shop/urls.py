from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('',views.base,name='base'),
    path('<str:name>',views.filtr,name='filtr'),
    path('product/<str:pk>',views.product,name='product'),
    path('kontakt/',views.kontakt,name='kontakt'),
    path('o_nas/',views.o_nas,name='o_nas'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)