n,m=map(int,input().split())


lst=[]
def dfs(k):
    global lst
    if k==m:
        print(*lst)
        return
    for i in range(1,n+1):
        lst.append(i)
        dfs(k+1)
        lst.pop()

dfs(0)
