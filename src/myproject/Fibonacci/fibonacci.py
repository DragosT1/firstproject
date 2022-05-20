def fibonacci(nterms):
    # Program to display the Fibonacci sequence up to n-th term

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms > 1000000:
        print("Please enter an integer < 1M")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci Nth number of the sequence:")
        while count < nterms:

            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
        print(n1)
        return n1