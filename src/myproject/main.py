from myproject.parserart.parseArticle import *
from myproject.Fibonacci.fibonacci import *



if __name__ == "__main__":
    path = "/Users/user/work/firstproject/articleInput.txt"
    parseArticleSuite(path)

    nterms = int(input("How many terms? "))
    fibonacci(nterms)
