from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.
#cart is a customer property
# cart is the stage that order is not confirmed yet
class Order(models.Model):
    LIVE =1
    DELETE =0
    delete_choice =((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED =1
    ORDER_PROCESSED =2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    # Creating a tuble for status choice
    STATUS_CHOICE =((ORDER_PROCESSED,'ORDER_PROCESSED'),
                    (ORDER_DELIVERED,'ORDER_DELIVERED'),
                    (ORDER_REJECTED,'ORDER_REJECTED'))
    order_status = models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    
    # one user itself have many cart, so it should be one to many type
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL, null = True, related_name='orders')
    total_price =models.FloatField(default=0)
    delete_status= models.IntegerField(choices=delete_choice,default= LIVE)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "order-{}-{}".format(self.id, self.owner.user.username)

# each items in the cart have a item with quantity and price   
class OrderedItem(models.Model):
    product = models.ForeignKey(Product, related_name='added_carts', on_delete= models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order,on_delete= models.CASCADE, related_name='added_items')
    
    
    
    
    