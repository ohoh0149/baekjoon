a,b=map(int,input().split())

result=-1
def dfs(k,x,y):
    global result
    if x>y:
        return
    if x==y:
        result=max(result,k+1)
        return
    dfs(k+1,2*x,y)
    dfs(k+1,int(str(x)+"1"),y)

dfs(0,a,b)
print(result)