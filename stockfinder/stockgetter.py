from ystockquote import get_price, get_change, get_volume
from urllib2 import *
def price(ticker):
    '''
    For a given 'ticker' this function returns a dict containing
    {'ticker':'T', price:'P'}
    (Can lookup towards yahoo finance or even better - use live data
    from SEB )
    '''
    price = get_price(ticker)
    data = {'ticker': ticker, 'price': price}
    return data
def change(ticker):
	change = get_change(ticker)
	data = {'ticker': ticker, 'change':change}
	return data
def volume(ticker):
	volume = get_volume(ticker)
	data = {'ticker': ticker, 'volume': volume}
	return data
def netfonds_price(ticker):
	base_url = 'http://www.netfonds.no/quotes/tradedump.php?paper='
	datatype_url = '&csv_format=txt'
	url = base_url + ticker + datatype_url
	raw_data = urlopen(url).readlines()
	last_line = raw_data[len(raw_data)-1]
	datasplit = last_line.split('\t')
	price = datasplit[1]
	data = {'ticker': ticker, 'price': price}
	return data