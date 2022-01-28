from django.shortcuts import render
from .models import *
from cart.forms import CartAddProductForm

# Create your views here.
def store(request):
    products = Product.objects.all()
    cart_product_form = CartAddProductForm()
    context = {'products': products, 'cart_product_form': cart_product_form}
    return render(request, 'market/store.html', context)

