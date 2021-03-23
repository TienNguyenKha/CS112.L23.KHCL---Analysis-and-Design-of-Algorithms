#Nhập n đoạn đường
n=int(input())
#Gía trị a[i] là lãi của từng đoạn
a=[int(i) for i in input().split()]
#từ yêu cầu bài toán: ta có thể dễ dàng nhận thấy tổng tại phần tử thứ i chính bằng f[i]=f[i-1]+a[i] (gán f[0]=a[0])
f=[0 for i in range(n)]
f[0]=a[0]
for i in range(1,n):
    f[i]=f[i-1]+a[i]
maxn=0
fmin=0
p=0
q=0
s=0
sumo=0
for i in range(0,n):
    if f[i]-fmin>maxn:
        maxn=f[i]-fmin
        p=s
        q=i
    sumo+=a[i]
    if sumo<0:
        sumo=0
        s=i+1
    fmin=min(fmin,f[i])
print(p+1,q+1,maxn)