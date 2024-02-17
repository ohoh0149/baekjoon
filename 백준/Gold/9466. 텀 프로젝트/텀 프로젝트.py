import sys
sys.setrecursionlimit(10 ** 5)

t=int(input())

def dfs(x):
    global result,cycle
    #print(x,cycle)
    if visited[lst[x]]==0:
        visited[lst[x]]=1
        cycle.append(lst[x])
        dfs(lst[x])
    else:
        if lst[x] in cycle:
            result-=len(cycle)-cycle.index(lst[x])




for _ in range(t):
    n=int(input())
    result=n

    lst=[0]+list(map(int,input().split()))
    visited=[0]*(n+1)

    for i in range(1,n+1):
        if visited[i]==1:
            continue
        #print("-----------")
        cycle=[i]
        visited[i]=1
        dfs(i)
    print(result)




