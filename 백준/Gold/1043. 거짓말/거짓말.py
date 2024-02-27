n,m=map(int,input().split())
know=list(map(int,input().split()))

know.pop(0)
know=set(know)

graph=[[] for _ in range(n+1)]
arr=[]
for _ in range(m):
    temp=list(map(int,input().split()))
    temp.pop(0)
    arr.append(temp)
    l=len(temp)
    for i in range(l):
        for j in range(i+1,l):
            graph[temp[i]].append(temp[j])
            graph[temp[j]].append(temp[i])


from collections import deque
def get_people(lst):
    result_set=set()
    visited=[0]*(n+1)
    for p in lst:
        if visited[p]==0:
            q=deque()
            q.append(p)
            visited[p]=1
            while q:
                x=q.popleft()
                for nx in graph[x]:
                    if visited[nx]==0:
                        visited[nx]=1
                        q.append(nx)
    for i in range(1,n+1):
        if visited[i]!=0:
            result_set.add(i)
    return result_set


result=0
for come_lst in arr:
    cur_set=get_people(come_lst)
    tt=know.intersection(cur_set)
    if not tt:
        result+=1
print(result)