#!/usr/bin/python
from __future__ import division
import datetime
import string
import randomdotorg
from decimal import *

# The moneyfmt function is a python recipie available from
# http://docs.python.org/2/library/decimal.html
def moneyfmt(value, places=2, curr='', sep=',', dp='.',
             pos='', neg='-', trailneg=''):
    """Convert Decimal to a money formatted string.

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
    q = Decimal(10) ** -places      # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = map(str, digits)
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else '0')
    build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))


class WSD(object):
  """Read WSD csv file, and add <YYYY-MM-DD HH:MM, wsd>"""

  def __init__(self, fname):
    self.f = open(fname, 'r+')
    self.lines = [line.strip() for line in self.f]
    self.lines = self.lines[1:] # drop the header

  def addrandom(self, r):
    """Append r, checklength >= 600 and drop first"""
    if len(self.lines) >= 600:
      self.lines = self.lines[1:]
    wsd = moneyfmt(Decimal(r.randint(5,145))/Decimal('100'))
    self.lines = ["Date,WSD/USD"] + \
		 self.lines + \
       [datetime.datetime.today().strftime("%Y-%m-%d %H:%M") + ',' + wsd]    
    self.f.seek(0)
    for item in self.lines:
      self.f.write("%s\n" % item)
    self.f.truncate()
    self.f.close()

if __name__ == '__main__':
  r = randomdotorg.RandomDotOrg()
  if r.get_quota() < 0:
    exit (-1)
  wsd = WSD('wsd.csv') 
  wsd.addrandom(r)
