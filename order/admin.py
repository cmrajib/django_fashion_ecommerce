from django.contrib import admin

# Register your models here.
from order.models import Cart, Order

admin.site.register(Cart)
admin.site.register(Order)