from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from .models import inventory,Product,Sells
# Create your views here.


def Home(request):
    # context = {}
    context = inventory.objects.all()
    return render(request,"index.html",context={'dataset':context})

def products(request):
    """
    
    Function to print products

    """
    context = Product.objects.all()
    return render(request,"products.html",context={'dataset':context})


def sells(request):
    """
    
    Function to print sells products

    """
    context = Sells.objects.all()
    return render(request,"sell.html",context={'dataset':context})


class ProductCreateView(CreateView):

    model = Product
    fields = ('__all__')
    template_name = "addProduct.html"
    success_url = '/products'
class ProductUpdateView(UpdateView):
    model = Product
    # fields = ('__all__')
    template_name = "updateProduct.html"

