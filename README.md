# A little CLI to keep me informed of the availability of vegan donuts near me.

### Dependencies:
requests - run `pip install requests`
## Usage:
```
usage: vdonut [-h] [-f FILE] [-d DIET] [-l LOCATION] {config} ...

positional arguments:
  {config}

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Filename to write output to.
  -d DIET, --diet DIET  Dietary preferences. Use 'omni' if you have no
                        preference. 'vegan' and 'paleo' are also valid
                        options.
  -l LOCATION, --location LOCATION
                        The store location to get inventory from. Valid
                        Choices: franklin, east_nashville, west_nashville,
                        hillsboro, ponce_city_market, westside_provisions
```
