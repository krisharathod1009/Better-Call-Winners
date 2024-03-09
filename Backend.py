from selenium import webdriver
from bs4 import BeautifulSoup
import json
from urllib.parse import quote
from flask import Flask, jsonify, send_from_directory
import os
import pyautogui

# Set up the Selenium driver
# Assuming ChromeDriver is in the current working directory
driver = webdriver.Chrome()

# # Accept user input for the search query
# search_query = 'SSD Sata 1TB'
# # URL encode the search query
# encoded_query = quote(search_query)

with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
# Construct the URL with the encoded search query
# url = f'https://www.smartprix.com/products/?q={encoded_query}'
# print(url)

# Use Selenium to navigate to the URL
driver.get(content)

# Wait for the dynamic content to load (adjust the wait time as necessary)
driver.implicitly_wait(10)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

products_info = []
products_div = soup.find_all('div', class_='pg-prd-main-right') # Assuming 'sm-product' is the correct class for individual products
# print(products_div)

co1_list = []
co2_list = []
co3_list = []

for product in products_div:
    name = product.find('div', class_='pg-prd-head').text if product.find('div', class_='pg-prd-head') else None
    price = product.find('div', class_='price').text if product.find('div', class_='price') else None
    co_elements = product.find_all('div', class_='name')
    co1 = co_elements[0].text if co_elements else None
    co2 = co_elements[1].text if co_elements else None
    co3 = co_elements[2].text if co_elements else None
    # co_url = product.find_all('src', class_='')
    co_price = product.find_all('span', class_='price')
    # co1_url = product.find('src', class_='').text if product.find('src', class_='') else None
    # co2_url = product.find('src', class_='').text if product.find('src', class_='') else None
    # co3_url = product.find('src', class_='').text if product.find('src', class_='') else None
    # co1_price = product.find('span', class_='price').text if product.find('span', class_='price') else None
    # co2_price = product.find('span', class_='price').text if product.find('span', class_='price') else None
    # co3_price = product.find('span', class_='price').text if product.find('span', class_='price') else None
    # co1_url = co_url[0].text if co_elements else None
    # co2_url = co_url[1].text if co_elements else None
    # co3_url = co_url[2].text if co_elements else None

    co1_price = co_price[0].text if co_elements else None
    co2_price = co_price[1].text if co_elements else None
    co3_price = co_price[2].text if co_elements else None

    co1_list.append(co1)
    co1_list.append(co1_price)
    co2_list.append(co2)
    co2_list.append(co2_price)
    co3_list.append(co3)
    co3_list.append(co3_price)
    product_info = {
        'name': name,
        'price': price,
        'co1':co1_list,
        'co2':co2_list,
        'co3':co3_list
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
