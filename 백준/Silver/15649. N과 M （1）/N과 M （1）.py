n,m=map(int,input().split())

visited=[0]*(n+1)
cur_lst=[]
def dfs(k):
    global cur_lst
    if k==m:
        print(*cur_lst)
        return

    for i in range(1,n+1):
        if visited[i]==0:
            visited[i]=1
            cur_lst.append(i)
            dfs(k+1)
            cur_lst.pop()
            visited[i]=0

dfs(0)