

from django.db import models 



class SalesManager(models.Manager): 

    def get_total_sales_price(self, product):

        total_sales_price = 0 
        sales = self.filter(product=product)

        for sale in sales: 
            total_sales_price += sale.purchased_price

        return total_sales_price





    