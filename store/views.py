from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    template= "store/store.html"
    return render(request, template, context)
