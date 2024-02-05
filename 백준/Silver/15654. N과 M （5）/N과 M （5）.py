n,m=map(int,input().split())

input_lst=list(map(int,input().split()))

input_lst.sort()
lst=[]
visited=[0]*n
def dfs(k):
    global lst,visited
    if k==m:
        print(*lst)
        return
    for i in range(n):
        if visited[i]==1:
            continue
        lst.append(input_lst[i])
        visited[i]=1
        dfs(k+1)
        visited[i]=0
        lst.pop()

dfs(0)