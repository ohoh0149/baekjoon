def get_chi_len(x,y):
    min_len=1e9
    for cx,cy in cur_chi_lst:
        min_len=min(min_len,abs(cx-x)+abs(cy-y))
    return min_len


def get_result():
    res=0
    for hx,hy in house_lst:
        res+=get_chi_len(hx,hy)
    return res


def dfs(k,count):
    global cur_chi_lst
    global result
    if count>m:
        return
    if k==l :
        if count==m:
            result=min(get_result(),result)
        return
    dfs(k+1,count)

    cur_chi_lst.append(total_chi_lst[k])
    dfs(k+1,count+1)
    cur_chi_lst.pop()

result=1e9
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
total_chi_lst=[]
cur_chi_lst=[]
house_lst=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            house_lst.append((i,j))
        elif arr[i][j]==2:
            total_chi_lst.append((i,j))

l=len(total_chi_lst)
dfs(0,0)
print(result)