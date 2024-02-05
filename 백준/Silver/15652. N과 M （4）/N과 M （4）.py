n,m=map(int,input().split())


lst=[]
def dfs(k,num):
    global lst
    if k==m:
        print(*lst)
        return
    for i in range(num,n+1):
        lst.append(i)
        dfs(k+1,i)
        lst.pop()

dfs(0,1)