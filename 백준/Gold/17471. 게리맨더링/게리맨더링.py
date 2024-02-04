from collections import deque

n=int(input())
people_lst=list(map(int,input().split()))
arr=[[0]*n for _ in range(n)]
for i in range(n):
    temp_lst=list(map(int,input().split()))
    temp_lst.pop(0)
    for a in temp_lst:
        arr[i][a-1]=1
        arr[a-1][i]=1



cur_lst=[]
result=1e9
def check(cur_lst):

    q=deque()
    visited=[0]*n
    q.append(cur_lst[0])
    visited[cur_lst[0]]=1
    while q:
        x=q.popleft()
        for i in range(n):
            if i in cur_lst and visited[i]==0 and arr[x][i]==1:
                q.append(i)
                visited[i]=1
    if not sum(visited)==len(cur_lst):
        return False
    v=0
    for i in range(n):
        if i not in cur_lst:
            v=i
            break

    q=deque()
    visited=[0]*n
    q.append(v)
    for c in cur_lst:
        visited[c]=1
    visited[v]=1
    while q:
        x=q.popleft()
        for nx in range(n):
            if visited[nx]==0 and arr[x][nx]==1:
                q.append(nx)
                visited[nx]=1
    if sum(visited)==n:
        return True
    else:
        return False


total_people=sum(people_lst)
def dfs(k):
    global cur_lst,result
    if k==n:
        if 0<len(cur_lst)<n:
            if check(cur_lst):
                temp_people=0
                for c in cur_lst:
                    temp_people+=people_lst[c]
                result=min(result,abs(total_people-temp_people-temp_people))
        return
    dfs(k+1)
    cur_lst.append(k)
    dfs(k+1)
    cur_lst.pop()

dfs(0)

if result==1e9:
    print(-1)
else:
    print(result)