

cur_lst=[]
def dfs(k,count):
    global cur_lst
    if count>6:
        #print(*cur_lst)
        return
    if k==m:
        if count==6:
            print(*cur_lst)
        return
    cur_lst.append(lst[k])
    dfs(k+1,count+1)
    cur_lst.pop()
    dfs(k+1,count)
while True:
    lst=list(map(int,input().split()))
    m=lst.pop(0)
    if m==0:
        break

    dfs(0,0)


    print()
