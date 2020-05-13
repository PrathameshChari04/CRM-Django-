from django.contrib import admin

from .models import Customer
from .models import Product
from .models import Order
from .models import Tag

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
