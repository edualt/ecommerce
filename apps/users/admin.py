from django.contrib import admin
from apps.users.models import User
from apps.categories.models import Category
from apps.products.models import Product

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)