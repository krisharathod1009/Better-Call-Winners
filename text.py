from selenium import webdriver
from bs4 import BeautifulSoup
import json
from urllib.parse import quote

# Set up the Selenium driver
# Assuming ChromeDriver is in the current working directory
driver = webdriver.Chrome()

# Accept user input for the search query
search_query = input("Enter the product")
# URL encode the search query
encoded_query = quote(search_query)

# Construct the URL with the encoded search query
url = f'https://www.smartprix.com/products/?q={encoded_query}'
print(url)

# Use Selenium to navigate to the URL
driver.get(url)

# Wait for the dynamic content to load (adjust the wait time as necessary)
driver.implicitly_wait(10)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

products_info = []
products_div = soup.find_all('div', class_='sm-product') # Assuming 'sm-product' is the correct class for individual products
print(products_div)

for product in products_div:
    name = product.find('a', class_='name clamp-2').text if product.find('a', class_='name clamp-2') else None
    price = product.find('span', class_='price').text if product.find('span', class_='price') else None
    product_info = {
        'name': name,
        'price': price
        # Add more fields if needed
    }
    products_info.append(product_info)

with open('ecommerce_products.json', 'w') as file:
    json.dump(products_info, file, indent=4)

print('Scraping and JSON file creation successful!')

# Close the driver
driver.quit()
