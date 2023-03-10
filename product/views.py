

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny

from rest_framework import status 


from product.models import Product, Sales
from product.serializers import ProductSerializer

import pandas as pd 

class ProductAPI(ModelViewSet): 

    serializer_class = ProductSerializer
    permission_classes = (AllowAny, )
    queryset = Product.objects.all() 





class TotalSalesAPI(ViewSet): 

    def list(self, request): 

        serialized_data = list() 
        sales_df = None

        product_query = Product.objects.prefetch_related('sales')

        for product in product_query:

            total_price = Sales.objects.get_total_sales_price(product) 
            total_sales = Sales.objects.filter(product=product).count() 

            serializer = { 
                'product_name': product.product_name,
                'total_sales': total_sales,
                'total_price': total_price,
            }


            serialized_data.append(serializer)

        sales_df = pd.Series(serialized_data)
        return Response(status=status.HTTP_200_OK, data=sales_df)

