from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json



from urllib.parse import quote

# Set up the Selenium driver
driver = webdriver.Chrome()

# Navigate to the URL
search_query = 'redmi 12'
print(search_query)
# URL encode the search query
encoded_query = quote(search_query)

url = f'https://www.smartprix.com/products/?q={encoded_query}'
driver.get(url)

# Wait for the dynamic content to load
time.sleep(10)

# Find the element by its XPath and click on it to open a new tab
element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/main/div[1]/div[2]/div[2]/div[1]/a")
element.click()

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Wait for the new page to load
time.sleep(5)

# Copy the URL of the new tab
new_tab_url = driver.current_url
print("URL of the new tab:", new_tab_url)
with open('output.txt', 'w') as file:
    # Write the content of the variable to the file
    file.write(new_tab_url)
# Close the new tab and switch back to the original tab
driver.close()
driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()


driver = webdriver.Chrome()

# Accept user input for the search query

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

with open('products.json', 'w') as file:
    json.dump(products_info, file, indent=4)

print('Scraping and JSON file creation successful!')

# Close the driver


from flask import Flask, jsonify, send_from_directory
import os

# Create the Flask application instance
app = Flask(__name__)

@app.route('/specproducts', methods=['GET'])
def get_products():
    # Assuming the JSON file is named 'products.json'
    json_file_path = 'products.json'
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
    app.run(debug=True, host='0.0.0.0', port=5001)


driver.quit()