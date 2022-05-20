from myproject.parserart.parseArticle import *
from myproject.Fibonacci.fibonacci import *


def test_parseArticle():
    listinput = ['iceland', 'economy', 'weathered']
    c = countTotalWords(listinput)
    assert c == 3

def test_fibonnaci():
    var = fibonacci(70)
    assert var == 190392490709135