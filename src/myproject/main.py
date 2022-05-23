from myproject.parserart.parseArticle import *
from myproject.Fibonacci.fibonacci import *
from myproject.sortlist.sortlist import *


if __name__ == "__main__":
    path = "/Users/user/work/firstproject/articleInput.txt"
    parseArticleSuite(path)

    nterms = int(input("How many terms? "))
    fibonacci(nterms)

    list1 = [1, 5, 6, 9, 11]
    list2 = [3, 4, 7, 8, 10]

    sortlist(list1, list2)
