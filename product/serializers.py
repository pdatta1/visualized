
from rest_framework import serializers


from product.models import Product, Sales



class SalesSerializer(serializers.ModelSerializer): 

    product = serializers.ReadOnlyField(source='product.product_name')
    purchased_price = serializers.DecimalField(max_digits=100, decimal_places=2)

    class Meta: 
        model = Sales 
        fields = ('product', 'purchased_price')





class ProductSerializer(serializers.ModelSerializer): 

    product_name = serializers.CharField(max_length=30, min_length=5, allow_blank=False)
    sales = SalesSerializer(many=True)
    

    class Meta: 
        model = Product
        fields = ('product_name', 'sales')

