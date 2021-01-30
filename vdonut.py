#Hopefully this URL doesn't change
#https://five-daughters-bakery.square.site/s/order?location=11ea670d96d28035a53a0cc47a2b63cc

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://five-daughters-bakery.square.site/s/order?location=11ea670d96d28035a53a0cc47a2b63cc')

#To ensure that the page is loaded
time.sleep(5)

#This renders the JS code and stores all the info in static HTML.
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

products = soup.find_all('div', {'class': 'meta'})
# Can remove products maybe...
names = [product.find('p', {'class': 'w-product-title'}) for product in products]
availabilities = [product.find('div', {'class': 'stock-tag'}) for product in products]
prices = [product.find('span', {'class': 'font--product-price'}) for product in products]

for i in range(len(products)):
    if 'Vegan' in names[i].text:
        if availabilities[i]:
            print(prices[i].text.strip() + '  |  ' + names[i].text.strip() + '  |  ' + availabilities[i].text.strip())
        else:
            print(prices[i].text.strip() + '  |  ' + names[i].text.strip())