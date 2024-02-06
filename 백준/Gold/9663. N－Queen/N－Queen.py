n=int(input())

result=0
v1=[0]*n
v2=[0]*2*n
v3=[0]*2*n
def dfs(k):
    global result,v1,v2,v3
    if k==n:
        result+=1
        return
    for j in range(n):
        if v1[j]==0 and v2[k+j]==0 and v3[k-j]==0:
            v1[j],v2[k+j],v3[k-j]=1,1,1
            dfs(k+1)
            v1[j],v2[k+j],v3[k-j]=0,0,0
dfs(0)
print(result)