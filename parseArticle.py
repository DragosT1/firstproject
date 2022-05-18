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
    text = inputText.readlines()
    onestring = ""
    fullWordList = []
    char_to_replace = {'.': '',
                       ',': '',
                       '!': '',
                       '?': '',
                       '/': '',
                       '\n': '',
                       '-': '',
                       '_': '',
                       '’': ' ',
}
    # Build one string form all lines and make lowercase everything
    for i in range(0, len(text)):
        onestring = onestring + str(text[i]).lower()

    # Iterate over all key-value pairs in dictionary to remove unwanted signs
    for key, value in char_to_replace.items():
        # Replace key character with value character in string
        onestring = onestring.replace(key, value)
    
    #Iteration to remove prepositions
    for word in onestring.split(" "):
        if len(word) <= 3:
            word = ""
        else: fullWordList.append(word)
    #     print(word)
    # print(fullWordList)
    # print(onestring)
    return fullWordList

def findPhoneNb(listinput):
    list = []
    for word in listinput:
        if word[0] == "0" and len(word) == 10:
            list.append(word)
    print("Phone numbers: "+str(list))

def countTotalWords(listinput2):
    print("Total number of words: " + str(len(listinput2)))

def countUniqueWords(listinput3):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for word in listinput3:
        # check if exists in unique_list or not
        if word not in unique_list:
            unique_list.append(word)
    return unique_list

def top5Words (list1,list2):
    dicts = {}
    for wordUnique in range(len(list2)):
        dicts[list2[wordUnique]] = 0
        for allWords in range(len(list1)):
            if list1[allWords] == list2[wordUnique]:
                dicts[list2[wordUnique]] += 1


    sortedunuque = (sorted(dicts))
    print("top1 word appearance is: " + str(sortedunuque[len(sortedunuque)-1]))
    print("top2 word appearance is: " + str(sortedunuque[len(sortedunuque) - 2]))
    print("top3 word appearance is: " + str(sortedunuque[len(sortedunuque) - 3]))
    print("top4 word appearance is: " + str(sortedunuque[len(sortedunuque) - 4]))
    print("top5 word appearance is: " + str(sortedunuque[len(sortedunuque) - 5]))




def main():
    input = open("/Users/user/work/firstproject/articleInput.txt", "r")
    cleanedText = replaceUnwantedChar(input)
    findPhoneNb(cleanedText)
    countTotalWords(cleanedText)
    uniqueWordsList = countUniqueWords(cleanedText)
    print("Number of unique words is: " + str(len(uniqueWordsList)))
    top5Words(cleanedText, uniqueWordsList)

if __name__ == "__main__":
    main()
