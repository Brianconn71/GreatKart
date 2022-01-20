from django.shortcuts import render

# Create your views here.
def cart(request):
    template = 'store/cart.html'
    return render(request, template)
