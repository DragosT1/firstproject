from myproject.parserart.parseArticle import *
from myproject.Fibonacci.fibonacci import *
from myproject.divisors.divisors import *
from myproject.sortlist.sortlist import *


def test_parseArticle():
    listinput = ["iceland", "economy", "weathered"]
    c = countTotalWords(listinput)
    assert c == 3


def test_fibonnaci():
    var = fibonacci(70)
    assert var == 190392490709135


def test_divizori():
    var = divisors(24)
    assert var == [1, 2, 3, 4, 6, 8, 12, 24]


def test_sortlist():
    list1 = [1, 5, 6, 9, 11]
    list2 = [3, 4, 7, 8, 10]
    var = sortlist(list1, list2)
    assert var == [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
