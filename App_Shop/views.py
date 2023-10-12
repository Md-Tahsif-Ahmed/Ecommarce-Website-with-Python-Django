from django.shortcuts import render
# import view
from  django.views.generic import ListView, DetailView
# models
from App_Shop.models import Product
# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(ListView):
    model = Product
    template_name = 'App_shop/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'

 
