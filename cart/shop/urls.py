from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='trackerStatus'),
    path('search/', views.search, name='Search'),
    path('products/<int:myid>', views.productView, name='ProductView'),
    path('checkout/', views.checkout, name='CheckOut'),
    # path('handlerequest/', views.handlerequest, name='HandleRequest'),
    path('success', views.success, name='Success')
]
