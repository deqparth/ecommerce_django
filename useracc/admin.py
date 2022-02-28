from django.contrib import admin
from django.contrib.auth.models import Group

from useracc.models import User, Product

# Register your models here.
admin.site.register(User)
admin.site.register(Product)

admin.site.unregister(Group)
