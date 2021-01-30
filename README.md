# A little CLI to keep me informed of the availability of vegan donuts near me.

### Dependencies:
Selenium
Chrome
You'll need to download the `chromedriver` executable, with a version that matches
the version of your Chrome browser, and put that executable in a directory that's on `$PATH`.
To see $PATH, type `echo $PATH` in a terminal.

## Usage:
usage: vdonut [-h] [-o] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -o, --omni            Shows availability of all donuts, not just vegan ones.
  -f FILE, --file FILE  Filename to write output to.

## Coming Soon:
Option to show only paleo donuts
Show only food items
Option to choose Five Daughters Bakery locations
Configure your default options, such as diet and location
Lose dependency on selenium and Chrome.