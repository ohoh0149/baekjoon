from collections import deque

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    lst=list(map(int,input().split()))

    q=deque()
    temp_lst=[0]*10
    for idx,p in enumerate(lst):
        q.append((idx,p))
        temp_lst[p]+=1
    count=1
    while True:
        idx,p=q.popleft()
        #print(idx,p)
        is_max=True
        for i in range(p+1,10):
            if temp_lst[i]>0:
                is_max=False
                break
        if is_max:
            temp_lst[p]-=1
            if idx==m:
                break
            else:
                count+=1

            pass
        else:
            q.append((idx,p))
    print(count)


