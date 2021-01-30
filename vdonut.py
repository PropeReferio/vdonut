#!/usr/bin/env python

#Hopefully this URL doesn't change
#https://five-daughters-bakery.square.site/s/order?location=11ea670d96d28035a53a0cc47a2b63cc
import time
import datetime
import argparse

from selenium import webdriver
from bs4 import BeautifulSoup

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

def show_products():
	for i in range(len(products)):
		if 'Vegan' in names[i].text:
			if availabilities[i]:
				print(prices[i].text.strip() + '  |  ' + names[i].text.strip() + '  |  ' + availabilities[i].text.strip())
			else:
				print(prices[i].text.strip() + '  |  ' + names[i].text.strip())

def get_output(omni=False):
	output = str(datetime.datetime.now()) + '\n'
	if not omni:
		for i in range(len(products)):
			if 'Vegan' in names[i].text:
				if availabilities[i]:
					output += prices[i].text.strip() + '  |  ' + names[i].text.strip() + '  |  ' + availabilities[i].text.strip() + '\n'
				else:
					output += prices[i].text.strip() + '  |  ' + names[i].text.strip() + '\n'
	else:
		for i in range(len(products)):
			if availabilities[i]:
				output += prices[i].text.strip() + '  |  ' + names[i].text.strip() + '  |  ' + availabilities[i].text.strip() + '\n'
			else:
				output += prices[i].text.strip() + '  |  ' + names[i].text.strip() + '\n'
	return output

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-o", "--omni", help="Shows availability of all \
		donuts, not just vegan ones.", action="store_true")
	parser.add_argument("-f", "--file", help="Filename to write output to.",
	type=str)

	args = parser.parse_args()
	if args.omni:
		print("Showing omni donuts: ")
		output = get_output(args.omni)
	else:
		print("Showing vegan donuts only: ")
		output = get_output()
	
	print(output)

	if args.file:
		with open(args.file, "a") as f:
			f.write(output)

if __name__ == "__main__":
	Main()