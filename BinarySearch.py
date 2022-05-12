# Given a file called input.txt, which contains:
# on the first line, an integer number, called X
# on the second line, a list of N sorted integers separated by space, where 0 < N <= 10000
# write a python program that:
# prints the index (position in list) of the first occurrence of X, if X is in the list
# prints -1 if X is not in the list


def binarySearch(listelem, x , low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if int(listelem[mid]) == x:
            return mid

        elif int(listelem[mid]) < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

input = open("/Users/user/work/firstproject/input.txt", "r")
lines = input.readlines()
print(lines)
X = int(lines[0])
print(X)
listelem = lines[1].split()

result = binarySearch(listelem, X, int(listelem[0]), len(listelem)-1)

if result != -1:
    print("Element is present at index: " + str(result))
else:
    print("Not found exit with code: "+str(result))