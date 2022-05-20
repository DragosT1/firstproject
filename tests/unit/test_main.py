from myproject.parserart.parseArticle import *
from myproject.Fibonacci.fibonacci import *
from myproject.divisors.divisors import *

def test_parseArticle():
    listinput = ['iceland', 'economy', 'weathered']
    c = countTotalWords(listinput)
    assert c == 3

def test_fibonnaci():
    var = fibonacci(70)
    assert var == 190392490709135

def test_divizori():
    var = divisors(24)
    assert var == [1, 2, 3, 4, 6, 8, 12, 24]
