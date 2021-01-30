# A little CLI to keep me informed of the availability of vegan donuts near me.

### Dependencies:
Selenium
Chrome
You'll need to download the `chromedriver` executable, with a version that matches
the version of your Chrome browser, and put that executable in a directory that's on `$PATH`.
To see $PATH, type `echo $PATH` in a terminal.

## Usage:
usage: vdonut [-h] (-o | -p | -v) [-f FILE] -l LOCATION

optional arguments:
  -h, --help            show this help message and exit
  -o, --omni            Shows availability of all donuts.
  -p, --paleo           Shows availability of paleo donuts.
  -v, --vegan           Shows availability of vegan donuts.
  -f FILE, --file FILE  Filename to write output to.
  -l LOCATION, --location LOCATION
                        The store location to get inventory from. Valid
                        Choices: franklin east_nashville west_nashville
                        hillsboro ponce_city_market westside_provisions

## Coming Soon:
Configure your default options, such as diet and location
Lose dependency on selenium and Chrome.