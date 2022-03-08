from django.contrib import admin
from django.contrib.auth.models import Group

from useracc.models import User, Product, Cart, CartItems, Wishlist

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.unregister(Group)
