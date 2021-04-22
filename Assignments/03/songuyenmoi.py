temp=input()
n=list(map(int,list(temp)))
#kiểm tra xem số n phải cộng thêm bao nhiêu để chia hết cho 3? ví dụ 5%3=2
#tức (5+(3-2(modul từ kết quả chia dư trên))%3)=0
# tương đương với 5 +1=6 và 6%3=0
temp0=3-int(temp)%3
#vì tìm số nguyên lớn nhất nên ý tưởng sẽ đi từ số đầu tiên của list,ví dụ 123 sẽ đi từ hàng trăm xét dần đến hàng đơn vị
flag=0#nếu số đầu vào có thay đổi thì đổi flag=1
for i in range(len(n)):
    temp1=n[i]+temp0
    if temp1<=9:#nếu sau khi cộng vào số temp0 mà vẫn thuộc 0->9 thì xét số này
        while temp1<=6:#vì giả sử temp=6,==>6+3=9 ==>vẫn là 1 số
            temp1+=3
        n[i]=temp1
        flag=1
        break
if flag==0:#tức số đầu vào không có gì thay đổi==> tức tìm số lớn hơn số đầu vào là không thể vì có thể n[i]+temp0>9
#==> vậy ta tìm số bé hơn nhưng vẫn đảm bảo lớn nhất có thể và chia hết cho 3
#==> biến đổi hàng từ hàng đơn vị để được số lớn nhất có thể
    i=len(n)-1
    while i>=0:
        if temp0==3 and n[i]>=3:#tức số đầu vào đã chia hết cho 3==> chỉ cần trừ đi 3 để được số chia hết cho 3 nhưng vẫn lớn nhất
            n[i]-=3
            break
        elif temp0!=3 and n[i]>=int(temp)%3:
            n[i]-=int(temp)%3
            break
        i-=1
for i in range(len(n)):
    print(n[i],end='')
