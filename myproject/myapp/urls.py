from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('services/smm', views.smm, name='smm'),
    path('services/product-marketing', views.product_marketing, name='product_marketing'),
    path('services/automation', views.automation, name='automation'),
    path('contact', views.contact, name='contact'),
    path('learn', views.learn, name='learn'),
]
