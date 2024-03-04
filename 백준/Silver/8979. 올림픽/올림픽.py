n,k=map(int,input().split())
lst=[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    lst.append((b,c,d,a))

lst.sort(reverse=True)

for i in range(n):
    _,_,_,num=lst[i]
    if num==k:
        cur=i
        while cur>0:
            if lst[cur-1][:3]==lst[cur][:3]:
                cur-=1
            else:
                break
        print(cur+1)
        break
