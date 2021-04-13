def H_index(a, n):
    for i, ai in enumerate(a):
        result = n - i
        if result <= ai:
            return result
    return 0

n = int(input())
a = sorted(list(map(int, input().split())))

print(H_index(a, n))