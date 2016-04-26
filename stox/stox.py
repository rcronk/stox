""" stox.py - a python interface to Yahoo Finance. """
import sys

class Company(object):
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol

    def get_stock_price(self, time=None):
        return 9.99

def main():
    c = Company('goog')
    print(c.get_stock_price())

if __name__ == '__main__':
    sys.exit(main())