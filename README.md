This is an experimental site. Ultimately it will expose the world's financial mischief.
For now, it shows a time series graph of the USD exchange rate for the Wall Street Dollar,
the currency for exposure to conflict of interest risk in the financial markets. The
exchange rate tracks atmospheric noise.

The python script wsd.py retrieves a random number from random.org, and rewrites wsd.csv. 
One thousand pairs of the form "YYYY-MM-DD HH:MM, #.##" are written to wsd.csv; old
values are cycled out.  The output is formatted using a money formatting routine 
obtained from python.org.  The python library randomdotorg must 
be installed for wsd.py. 

Prerequisites:
pip install randomdotorg
Twitter's bootstrap html5,css,js library
dygraph

wsd.sh
The file wsd.sh is called by a crontab entry every few minutes; this
calls wsd.py and writes wsd.csv. The crontab line is
*/3 * * * * /var/www/html/wsd/wsd.sh
It should be installed as root



