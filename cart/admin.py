from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = 

admin.site.register(Cart)
admin.site.register(CartItem)