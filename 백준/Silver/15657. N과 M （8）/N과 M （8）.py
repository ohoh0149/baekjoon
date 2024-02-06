n,m=map(int,input().split())
lst=list(map(int,input().split()))

lst.sort()

cur_lst=[]
def dfs(k,count,last_idx):
    global cur_lst
    if k==m:
        print(*cur_lst)
        return
    for i in range(last_idx,n):
        cur_lst.append(lst[i])
        dfs(k+1,count+1,i)
        cur_lst.pop()


dfs(0,0,0)

