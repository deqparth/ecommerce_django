from django.contrib import admin
from django.contrib.auth.models import Group

from useracc.models import User, Product, Wishlist, Cart, CartItems, Order, OrderItems, Category, Brand

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(Brand)
