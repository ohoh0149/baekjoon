
from collections import deque

n,m=map(int,input().split())
lst=list(map(int,input().split()))


q=list(range(1,n+1))
result=0
while lst:
    num=lst.pop(0)
    l=len(q)
    idx=q.index(num)
    #print("idx",idx)

    if idx<=l//2:
        result+=idx
        q=q[idx+1:]+q[:idx]
    else:
        result+=l-idx
        q=q[idx+1:]+q[:idx]
    #print(result)
    #print(q)
print(result)



