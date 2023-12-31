from collections import deque

def get_count(n,graph,a,b):
    ab=[a,b]
    lst=[]
    for i in range(2):
        q=deque()
        visited=[0]*(n+1)
        q.append(ab[i])
        visited[ab[i]]=1
        count=1
        while q:
            x=q.popleft()
            for i in range(1,n+1):
                if visited[i]==0 and graph[x][i]==1:
                    q.append(i)
                    visited[i]=1
                    count+=1
        lst.append(count)
    return abs(lst[0]-lst[1])
        
        
    

def solution(n, wires):
    graph=[[0]*(n+1) for _ in range(n+1)]
    answer = 1e9
    for a,b in wires:
        graph[a][b]=1
        graph[b][a]=1
        #print(a,b)
    for a,b in wires:
        graph[a][b]=0
        graph[b][a]=0
        
        answer=min(answer,get_count(n,graph,a,b))
        
        
        graph[a][b]=1
        graph[b][a]=1
    return answer