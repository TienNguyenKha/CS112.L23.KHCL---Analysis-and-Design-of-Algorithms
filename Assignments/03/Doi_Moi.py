a,k,b,m,n = map(int,input().split())
days = n//(a+b)
trees=days*(a+b)-a*(days//k)-b*(days//m)
diff=n-trees
while (diff >= (a+b)) :
    days = days + diff//(a+b)
    trees=days*(a+b)-a*(days//k)-b*(days//m)
    diff=n-trees
while(trees < n):
    days+=1
    if days % k == 0:
        trees+=0
    else :
        trees+=a
    if days % m ==0:
        trees+=0
    else:
        trees+=b
print(days)