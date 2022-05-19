from myproject.waterbottle.bottle import drink
from myproject.parserart.parseArticle import *

from myproject.parserart.parseArticle import replaceUnwantedChar, findPhoneNb, countTotalWords, countUniqueWords, \
    top5Words


if __name__ == "__main__":

    input = open("parserart/parseArticle.py", "r")
    cleanedText = replaceUnwantedChar(input)
    findPhoneNb(cleanedText)
    countTotalWords(cleanedText)
    uniqueWordsList = countUniqueWords(cleanedText)
    print("Number of unique words is: " + str(len(uniqueWordsList)))
    top5Words(cleanedText, uniqueWordsList)
