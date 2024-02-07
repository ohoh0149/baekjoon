n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

pos_lst=[]
lst=[0]*2*n
for i in range(2*n):
    lst[i]=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            lst[i+j].append((i,j))
#print(lst)

v2=[0]*(2*n)
result=0
def dfs(k,count):
    global  result,v2
    if 2*n-1-k+count<=result:
        return
    if k==2*n-1:
        result=max(result,count)
        return

    for x,y in lst[k]:
        if v2[x-y]==0:
            v2[x-y]=1
            dfs(k+1,count+1)
            v2[x-y]=0
    dfs(k+1,count)

dfs(0,0)
print(result)


