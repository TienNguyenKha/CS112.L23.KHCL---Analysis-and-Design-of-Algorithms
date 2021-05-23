import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (d*a - b*c) >= 0:
    print(0)
else:
    count = 0
    while ((a*d != b*c) and ((a*d - b*c) < 0)):
        a = a + 1
        b = b + 1
        gcd = math.gcd(a, b)
        a = a//gcd
        b = b//gcd
        count = count + 1
    if (a*d - b*c) > 0 :
        print(0)
    else:
        print(count)