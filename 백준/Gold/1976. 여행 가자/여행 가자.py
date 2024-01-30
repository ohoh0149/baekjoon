from collections import deque

n=int(input())
m=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

route=list(map(int,input().split()))
route=list(map(lambda x:x-1,route))
cur=route[0]
isOk=True

def can(p1,p2):
    q=deque()
    visited=[0]*n
    q.append(p1)
    visited[p1]=1
    while q:
        p=q.popleft()
        if p==p2:
            return True
        for i in range(n):
            if arr[p][i]==1 and visited[i]==0:
                q.append(i)
                visited[i]=1
    return False


for i in range(1,m):
    next_cur=route[i]

    if can(cur,next_cur):
        cur=next_cur
    else:
        isOk=False
        break

if isOk:
    print("YES")
else:
    print("NO")

