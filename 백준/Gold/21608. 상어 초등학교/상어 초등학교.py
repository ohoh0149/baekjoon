n=int(input())

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def find_pos(num):
    max_val=(-1,-1)
    rx,ry=-1,-1
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                continue
            like_count=0
            blank_count=0
            for d in range(4):
                nx=i+dx[d]
                ny=j+dy[d]
                if in_range(nx,ny):
                    if arr[nx][ny]==0:
                        blank_count+=1
                    else:
                        if arr[nx][ny] in dic[num]:
                            like_count+=1
            if max_val<(like_count,blank_count):
                max_val=(like_count,blank_count)
                rx,ry=i,j
    return rx,ry

arr=[[0]*n for _ in range(n)]
num_lst=[]
dic=dict()
for _ in range(n*n):
    lst=list(map(int,input().split()))
    num=lst.pop(0)
    num_lst.append(num)
    dic[num]=set(lst)

for num in num_lst:
    x,y=find_pos(num)
    arr[x][y]=num

temp_lst=[0,1,10,100,1000]
result=0
for i in range(n):
    for j in range(n):
        count=0
        for d in range(4):
            nx=i+dx[d]
            ny=j+dy[d]
            if in_range(nx,ny) and arr[nx][ny] in dic[arr[i][j]]:
                count+=1
        result+=temp_lst[count]

print(result)

