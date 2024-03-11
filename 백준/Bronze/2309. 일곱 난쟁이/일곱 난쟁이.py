lst=[]
for _ in range(9):
    lst.append(int(input()))

lst.sort()

cur_lst=[]
def dfs(k,count,sm):
    if k==9:
        if count==7 and sm==100:
            for x in cur_lst:
                print(x)
            exit()
        return
    if count>7:
        return
    if 9-k+count<7:
        return

    dfs(k+1,count,sm)
    cur_lst.append(lst[k])
    dfs(k+1,count+1,sm+lst[k])
    cur_lst.pop()


dfs(0,0,0)