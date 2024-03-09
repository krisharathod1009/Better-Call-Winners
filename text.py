import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.smartprix.com/products'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    products_info = []
    products_div = soup.find('div', class_='sm-products')
    
    if products_div:
        products = products_div.find_all('div', class_='sm-products') # Assuming 'product-card' is the correct class for individual products
        for product in products:
            name = product.find('a', class_='name clamp-2').text if product.find('a', class_='name clamp-2') else None
            specs = product.find('span', class_='price').text if product.find('span', class_='price') else None

            product_info = {
                'name': name,
                'specs': specs
                # Add more fields if needed
            }
            products_info.append(product_info)

        with open('ecommerce_products.json', 'w') as file:
            json.dump(products_info, file, indent=4)

        print('Scraping and JSON file creation successful!')
    else:
        print('No products found on the page.')
else:
    print('Failed to retrieve the webpage.')
