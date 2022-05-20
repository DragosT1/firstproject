def divisors(n):
    result = set()
    # n**0.5 square root
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    print("Divisors of:" + str(n))
    print(list(result))
    return list(result)