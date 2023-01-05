
from product.models import Product, Sales
import product as product_module
from progress.bar import Bar 

import json 
import os 
import random 


def create_file_dir( directory ): 

    file_module = os.path.dirname(product_module.__file__)
    file_dir = os.path.join(file_module, directory)
    return file_dir


def generate_product_data( directory ): 

    file_directory = create_file_dir(directory)

    with open(file_directory, 'r') as product_file: 

        data = product_file.read() 
        product_dict = json.loads(data)
        progress = Bar('Generating Product Data', max=len(product_dict))

        for product in product_dict: 

            Product.objects.create(**product)
            progress.next() 

        progress.finish() 


def generate_sales_data( directory ): 

    file_directory = create_file_dir(directory)
    product_query = Product.objects.all() 

    with open(file_directory, 'r') as mock_data: 

        data = mock_data.read() 
        sales = json.loads(data)

        progress = Bar('Generating Sales Data', max=len(sales))

        for product in product_query: 

            random_sales_count = random.randint(10, 100)
            sampled_sales = random.sample(sales, random_sales_count)

            for sale in sampled_sales: 

                Sales.objects.create(product=product, **sale)
            progress.next() 

        progress.finish() 


def cleanup(): 

    Product.objects.all().delete() 
    Sales.objects.all().delete()     

    


cleanup() 
generate_product_data('product_mock.json') 
generate_sales_data('sales_mock.json')
