#TODO: Implement function
def find(ticker):
    '''
    For a given 'ticker' this function returns a dict containing
    {'ticker':'T', price:'P'}
    (Can lookup towards yahoo finance or even better - use live data
    from SEB )
    This version, a striped version of Corey Goldberg's ystockquote, fetches data from yahoo finance.
    '''
    import urllib
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (ticker, 'l1')
    price = urllib.urlopen(url).read().strip().strip('"')
    dictionary = {'ticker': ticker, 'price': price}
    return dictionary
