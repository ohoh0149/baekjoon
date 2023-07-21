n=int(input())
a_lst=list(map(int,input().split()))
b,c=map(int,input().split())

c_lst=[0]*n

for i in range(n):
    if a_lst[i]-b<0:
        continue
    if (a_lst[i]-b)%c==0:
        c_lst[i]=(a_lst[i]-b)//c
    else:
        c_lst[i]=(a_lst[i]-b)//c +1
#print(c_lst)
print(sum(c_lst)+n)

