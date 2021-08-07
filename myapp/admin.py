from django.contrib import admin
from .models import Location, Restaurant, Menu, Discount, Orders

admin.site.register(Location)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Discount)
admin.site.register(Orders)

