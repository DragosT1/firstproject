# given an integer N, 2 < N < 2 000 000, print (or write to a file) all the prime numbers smaller than it

def isPrime(number):
    # Number needs to be > 1
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# Function to print primes
def printPrime(number):
    for i in range(2, number + 1):
        if isPrime(i):
            print(i, end=" ")


number = int(input("Input a number >2 and <2000000: "))
if (number in range(3,2000000)):
    printPrime(number)
else:
    print("The number needs to be >2 and < 2000000")