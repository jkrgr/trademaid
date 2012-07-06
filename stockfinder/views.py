"""
This module contains a set of help functions that interact with a
stock market API (f.ex. Yahoo Finance). The functions typically
fetch data from the web and return it as dicts for the other views
to enjoy.
"""
import stockgetter

def stockfinder_view(request):
    '''
    This view displays a HTML-page where the user can search for stocks
    on the OSL stock exchange.
    '''
    pass

class UserAction:
    pass

def buy(user_id, ticker, amount, price):
    '''
    This view lets a User, with id user_id, buy "amount" number of stocks
    with ticker name ticker, to the price of "price" pr stock.
    '''
    pass

def sell(user_id, ticker, amount, price):
    '''
    This view lets a User, with id user_id, sell "amount" number of stocks
    with ticker name ticker, to the price of "price" pr stock.
    '''
    pass

def watch(user_id, ticker):
    '''

    '''