from ystockquote import get_price, get_change, get_volume
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