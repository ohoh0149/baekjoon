n,m=map(int,input().split())


lst=[]
def dfs(k,count):
    global lst
    if count>m:
        return
    if k==n:
        if count==m:
            print(*lst)
        return

    lst.append(k+1)
    dfs(k+1,count+1)
    lst.pop()

    dfs(k+1,count)

dfs(0,0)