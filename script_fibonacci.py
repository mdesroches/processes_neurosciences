def fibonacci(n):
    """ Fibonacci sequence:
          f(1) = f(2) = 1 [or f(0) = 0 and f(1) = 1]
          f(n) = f(n-1)+f(n-2)  n>2
        input n, output f(n)
    """
    # for n= 1 and 2:
    if n <= 2:
        return 1
    # for n > 2
    f2, f1 = 1, 1
    # iterations
    for i in range(2, n+1):
        f2, f1 = f1, f1 + f2
    return f2        # value of f(n)

print("compute the n-th value of the Fibonacci sequence")
n = int(input("   value of n : "))
print("   fibonacci({}) = {}".format(n, fibonacci(n)))
