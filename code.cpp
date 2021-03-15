int Fib1(int n){
    int a, b, c;
    if (n <= 1)
        return n;
    a = 0; b = 1; c = 0;
    for (int k = 2; k <= n; k++) {
        c = a + b;
        a = b;
        b = c;
    }
    return c;
}

int Fib2(int n){
    if (n <= 1)
        return n;
    return Fib2(n - 1) + Fib2(n - 2)
}

s = 0;
for(i = 0; i <= n; i++){
    p = 1;
    for(j = 1; j <= i; j++)
        p = p * x / j;
    s += p;
}
