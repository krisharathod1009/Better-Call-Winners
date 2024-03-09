import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import quote # Import quote function for URL encoding

# Accept user input for the search query
#search_query = input("Enter the product you're searching for: ")
search_query = 'iphone 15'
# URL encode the search query
encoded_query = quote(search_query)

# Construct the URL with the encoded search query
url = f'https://www.smartprix.com/products/?q={encoded_query}'
print(url)
# url = 'https://www.smartprix.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    products_info = []
    products_div = soup.find_all('div', class_='sm-product') # Assuming 'sm-product' is the correct class for individual products
    print(products_div)
    for product in products_div:
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
    print('Failed to retrieve the webpage.')
