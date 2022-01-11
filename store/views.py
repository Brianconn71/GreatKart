from django.shortcuts import render
from .models import Product

# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()
    
    context = {
        'products': products,
        'product_count': product_count,
    }
    template= "store/store.html"
    return render(request, template, context)
