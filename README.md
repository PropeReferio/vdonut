# A little CLI to keep me informed of the availability of vegan donuts near me.

![Gif of Application at Work](./gif/normal_use.gif "A look at the application at work")

### Dependencies:
requests - run `pip install requests`

## Usage:
You can run this script from the directory that contains it by running `vdonut`.
If you add that directory to the `$PATH`, you'll be able to run it from anywhere.

Start by running `vdonut config` to set your default location and diet.
To override defaults, you could run `vdonut --location franklin --diet paleo`.
Once you have defaults the way you want them, you can simply run `vdonut`.

## Config Demo:
![Gif of Config at Work](./gif/config.gif "A look at the config at work")

```
vdonut --help
usage: vdonut [-h] [-f FILE] [-d DIET] [-l LOCATION] {config} ...

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

config:
  Running 'vdonut config' will set default arguments for location and diet.

  {config}
```
