from django.shortcuts import render

# Create your views here.

def _cart_id(request):
    

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.ogjects.get(cart_id=)


def cart(request):
    template = 'store/cart.html'
    return render(request, template)
