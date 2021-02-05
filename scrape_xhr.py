import requests

url = 'https://five-daughters-bakery.square.site/app/store/api/v13/editor/users/1312\
44516/sites/615594293746718473/store-locations/11ea670d998fb98ca53a0cc47a2b63cc/\
products?page=1&per_page=200&include=images,categories&has_categories=1&fulfillments[]=pickup'

r = requests.get(url)

data = r.json()['data']
names, high_prices, low_prices, availabilities = [], [], [], []
for i in data:
	names.append(i['name'])
	high_prices.append(i['price']['high_formatted'])
	low_prices.append(i['price']['low_formatted'])
	stock = i['badges']
	if stock['low_stock']:
		availabilities.append('Low Stock')
	elif stock['out_of_stock']:
		availabilities.append('Out of Stock')
	else:
		availabilities.append('')
print(str(len(names)), 'Names', str(len(low_prices)), 'Low Prices', str(len(high_prices)),\
 'High Prices', str(len(availabilities)), 'Availabilities')