from django.contrib import admin
from . models import seller, product, buyer
# Register your models here.
admin.site.register(seller)
admin.site.register(buyer)
admin.site.register(product)