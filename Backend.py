from selenium import webdriver
from bs4 import BeautifulSoup
import json
from urllib.parse import quote
from flask import Flask, jsonify, send_from_directory
import os

# Set up the Selenium driver
# Assuming ChromeDriver is in the current working directory
driver = webdriver.Chrome()

# Accept user input for the search query
search_query = 'iphone 15'
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

# Flask app setup
app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    # Assuming the JSON file is named 'ecommerce_products.json'
    json_file_path = 'ecommerce_products.json'
    if os.path.exists(json_file_path):
        # Use 'path' instead of 'filename'
        return send_from_directory(directory=os.path.dirname(json_file_path), path=os.path.basename(json_file_path))
    else:
        return jsonify({"error": "File not found"}), 404

@app.after_request
def set_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
