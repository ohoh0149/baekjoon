def in_range(x,y):
    return 0<=x<10 and 0<=y<10

def check(x,y,length):
    for i in range(x,x+length):
        for j in range(y,y+length):
            if not in_range(i,j) or  arr[i][j]==0:
                return False
    return True

def fill(x,y,length,num):
    global arr
    for i in range(x,x+length):
        for j in range(y,y+length):
            arr[i][j]=num


def dfs(k,idx):
    global arr
    global m_lst
    global result
    if k>=result:
        return
    if idx==l:
        result=min(result,k)
        return
    if k==l:
        return
    flag=False

    for i in range(idx,l):
        x,y=one_pos_lst[i]
        if arr[x][y]==1:
            idx=i
            nx,ny=x,y
            flag=True
            break
    #print(nx,ny)
    if not flag:
        result=min(result,k)
        return

    for num in range(5,0,-1):
        if m_lst[num]>0 and check(nx,ny,num):
            fill(nx,ny,num,0)
            m_lst[num]-=1
            dfs(k+1,idx+1)
            fill(nx,ny,num,1)
            m_lst[num]+=1




arr=[list(map(int,input().split())) for _ in range(10)]
one_pos_lst=[]
m_lst=[5]*6
result=1e9
for i in range(10):
    for j in range(10):
        if arr[i][j]==1:
            one_pos_lst.append((i,j))

l=len(one_pos_lst)

dfs(0,0)
if result==1e9:
    result=-1
print(result)