def fibonacci(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    c = 0

    for i in range(2, n + 1):
        c = a + b;
        a = b;
        b = c

    return c

n, k = map(int, input().split())
print(n * fibonacci(2 * k + 1) % (pow(10, 9) + 7))