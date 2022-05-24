# Given a piece of text( article), extract the following:
# How many words are there in total
# How many unique words are there
# What are the top 5 words that appear in the text ? What are their number of appearances?
# Print all phone numbers
# input file: input.txt
# file is openable
# what is a word?
# split by space
# remove all the punctuation
# don’t count words with less than 3 characters


def replaceUnwantedChar(inputText):
    onestring = inputText.read().lower()

    fullWordList = []
    char_to_replace = {
        ".": "",
        ",": "",
        "!": "",
        "?": "",
        "/": "",
        "\n": "",
        "-": "",
        "_": "",
        "’": " ",
    }

    # Iterate over all key-value pairs in dictionary to remove unwanted signs
    for key, value in char_to_replace.items():
        # Replace key character with value character in string
        onestring = onestring.replace(key, value)

    # Iteration to remove prepositions
    for word in onestring.split(" "):
        if len(word) <= 3:
            word = ""
        else:
            fullWordList.append(word)

    return fullWordList


def findPhoneNb(listinput):
    list = []
    for word in listinput:
        if word[0] == "0" and word[1] == "7" and word[2] != "0" and len(word) == 10:
            list.append(word)
    print("Phone numbers: " + str(list))


def countTotalWords(listinput2):
    print("Total number of words: " + str(len(listinput2)))
    return len(listinput2)


def countUniqueWordsTOP5(listinput3):
    # initialize a null list
    unique_list = []
    dicts = {}

    # traverse for all elements
    for word in listinput3:
        # check if exists in unique_list or not
        if word not in unique_list:
            unique_list.append(word)

    # Build dict from known unique words as keys and count key appearances
    for element in unique_list:
        dicts[element] = 0
        for allword in listinput3:
            if allword == element:
                dicts[element] += 1
    # Sort dict and print top 5 key appearances
    sortedunuque = sorted(dicts.items(), key=lambda val: val[1], reverse=True)
    # print(sortedunuque)
    for topWords in range(5):
        print("top" + str(topWords + 1) + " word appearance is: " + str(sortedunuque[topWords]))

    return unique_list


def parseArticleSuite(path):
    input = open(path, "r")
    cleanedText = replaceUnwantedChar(input)
    findPhoneNb(cleanedText)
    countTotalWords(cleanedText)
    uniqueWordsList = countUniqueWordsTOP5(cleanedText)
    print("Number of unique words is: " + str(len(uniqueWordsList)))
