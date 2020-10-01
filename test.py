from flask import flask
from unittest import TestCase
from app import app

def currency_checker(start, new, ammount):
    """Check that currency conversion is working properly"""

    newamount = str(round(c.convert(start, new, amount),2))
    return newamount

assert currency_checker(USD, USD, 1) == 1
assert currency_checker(USD, USD, 56.63) == 56.63
assert currency_checker(USD, USD, 100) == 100
assert currency_checker(EUR, EUR, 34) == 34
assert currency_checker(JPY, JPY, 20) == 20
