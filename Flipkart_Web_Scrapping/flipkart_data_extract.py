from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the webdriver (ensure you have downloaded the appropriate driver and provide its path)
driver = webdriver.Firefox()

# Open Flipkart
driver.get('https://www.flipkart.com/')

# Close the login popup if it appears
try:
    close_login_popup = driver.find_element(By.XPATH, '//button[contains(text(), "✕")]')
    close_login_popup.click()
except:
    pass

# Search for a product, e.g., 'laptops'
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('laptops')
search_box.send_keys(Keys.RETURN)

# Wait for the results to load
time.sleep(5)

# Scrape product details
products_Details = driver.find_elements(By.CSS_SELECTOR, "div[class='DOjaWF gdgoEp']")

print(products_Details)

for product in products_Details:
    product_details = product.find_elements(By.CLASS_NAME, "tUxRFH")
    print(product_details)
    for individual_product in product_details:
        Product_Name = individual_product.find_element(By.CLASS_NAME, "KzDlHZ").text
        Product_Spec = individual_product.find_element(By.CLASS_NAME, "_6NESgJ").text
        Product_Price = individual_product.find_element(By.XPATH, ".//div[starts-with(@class, 'Nx9bqj')]").text
        print(Product_Name +" "+Product_Spec +" " +Product_Price)

# Close the browser
driver.quit()
