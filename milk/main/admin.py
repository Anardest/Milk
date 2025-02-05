from django.contrib import admin
from .models import User, SupplierOrder, RecyclerOrder

admin.site.register(User)
admin.site.register(SupplierOrder)
admin.site.register(RecyclerOrder)
