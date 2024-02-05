n,m=map(int,input().split())

input_lst=list(map(int,input().split()))
input_lst.sort()

cur_lst=[]
def dfs(k,count):
    global cur_lst
    if count>m:
        return
    if k==n:
        if count==m:
            print(*cur_lst)
        return

    cur_lst.append(input_lst[k])
    dfs(k+1,count+1)
    cur_lst.pop()
    dfs(k+1,count)
dfs(0,0)
