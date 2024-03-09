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
