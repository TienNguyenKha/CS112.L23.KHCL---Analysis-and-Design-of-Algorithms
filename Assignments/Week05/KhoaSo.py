import io,os,sys
input=sys.stdin.readline 
k=input().strip()
k1=list(map(int,k))
k1.sort()
du=sum(k1)%3
if du==0:
    k1.reverse()
elif du==1:
    flag=0
    for i in k1:
        if i%3==1:
            k1.remove(i)
            flag=1
            break
    if flag==0:
        count=0
        for i in k1:
            if i%3==2:
                k1.remove(i)
        for i in k1:
            if i%3==2:
                k1.remove(i)
    k1.reverse()
else:
    flag=0
    for i in k1:
        if i%3==2:
            k1.remove(i)
            flag=1
            break
    if flag==0:
        count=0
        for i in k1:
            if i%3==1:
                k1.remove(i)
        for i in k1:
            if i%3==1:
                k1.remove(i)
        
    k1.reverse()
sys.stdout.write(''.join(map(str, k1[0:])))
    

