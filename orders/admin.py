from django.contrib import admin
from orders.models import Order,OrderedItem

# Register your models here.
#To see our order details from backend admin, we have to register

class OrderAdmin(admin.ModelAdmin):
    list_filter = [
        "owner",
        "order_status"
    ]
    search_fields =(
        "owner",
        "id"
    )
admin.site.register(Order,OrderAdmin)
