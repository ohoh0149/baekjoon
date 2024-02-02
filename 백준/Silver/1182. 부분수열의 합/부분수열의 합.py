n,s=map(int,input().split())
lst=list(map(int,input().split()))

result=0
count=0
temp_lst=[]
def dfs(k,sm):
    global temp_lst
    global count
    count+=1
    global result
    if k==n:
        if sm==s and temp_lst:
            result+=1
        return
    temp_lst.append(lst[k])
    dfs(k+1,sm+lst[k])
    temp_lst.pop()
    dfs(k+1,sm)

dfs(0,0)
print(result)