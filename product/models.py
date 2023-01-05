from django.db import models

from product.manager import SalesManager

class Product(models.Model): 

    product_name = models.CharField(max_length=30, null=False)


class Sales(models.Model): 

    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='sales')
    purchased_price = models.DecimalField(max_digits=100, decimal_places=2)

    objects = SalesManager() 





    