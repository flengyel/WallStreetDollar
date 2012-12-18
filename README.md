## The Wall Street Dollar ##
### The currency for exposure to conflict of interest risk ###

This is an experimental site. Ultimately it will expose the world's 
financial mischief.  For now, it shows a time series graph of the USD 
exchange rate for the Wall Street Dollar, the currency for exposure to 
conflict of interest risk in the financial markets. The WSD/USD spot
exchange rate shows the value of one Wall Street Dollar in US Dollars,
and tracks atmospheric noise. The value is updated every three minutes.

The python script wsd.py retrieves a random number from random.org, and 
rewrites wsd.csv. The file wsd.csv is a comma-separated file containing
the header "Date,USD/CSV", followed by  600 pairs of the form 
"YYYY-MM-DD HH:MM, #.##";  written to wsd.csv; old values are cycled out
by wsd.py.  The output is formatted using a money formatting routine obtained 
from python.org.  The python library randomdotorg must be installed for 
wsd.py. 

The Dygraph display shows the WSD/USD spot exchange rate at dates and times 
for five 120 point times spaced 3 minutes apart, beginning at midnight, 
Eastern Standard Time.  One day equals 420 points. The display of 600 points 
will ensure that at least one date will be visible on the display.

The file wsd.sh is called by a crontab entry every few minutes; this
calls wsd.py and writes wsd.csv. The crontab line is something like
*/3 * * * * /var/www/html/wsd/wsd.sh


## Prerequisites ##
* [RandomDotOrg](http://code.google.com/p/randomdotorg/)
* [Twitter's Bootstrap](http://twitter.github.com/bootstrap/) (html5,css,js) library
*  Dygraphs [dygraph-combined.js](https://github.com/danvk/dygraphs)
* [moneyfmt](http://docs.python.org/2/library/decimal.html#recipies)

## License ##

(c) 2010-2012, Florian Lengyel florian.lengyel@gmail.com
The text is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA-3.0)  license](http://creativecommons.org/licenses/by-nc-sa/3.0/).  My code is licensed under the GNU General Public License, version 2. All other code (bootstrap, randomdotorg, dygraph) is licensed separately.
Twitter's Bootstrap is licensed under the 
[Apache License v2.0](http://www.apache.org/licenses/LICENSE-2.0). 
Dygraphs is [copyright (c) 2009 Dan Vanderka](https://github.com/danvk/dygraphs/blob/master/LICENSE.txt), as in LICENCE.txt. 
RandomDotOrg is licensed under the [GPL v3](http://www.gnu.org/licenses/gpl.html).
