n,m=map(int,input().split())
arr=[[0]*(m+1) for _ in range(n+1)]
q_lst=list(map(int,input().split()))
q_num=q_lst.pop(0)
k_lst=list(map(int,input().split()))
k_num=k_lst.pop(0)
p_lst=list(map(int,input().split()))
p_num=p_lst.pop(0)

for i in range(0,2*p_num,2):
    arr[p_lst[i]][p_lst[i+1]]=-1


dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]
def in_range(x,y):
    return 1<=x<n+1 and 1<=y<m+1
for i in range(0, 2 * k_num, 2):
    kx, ky = k_lst[i], k_lst[i + 1]
    arr[kx][ky]=-1
    for d in range(8):
        nx=kx+dx[d]
        ny=ky+dy[d]
        if in_range(nx,ny) and arr[nx][ny]==0:
            arr[nx][ny]=1

# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(arr[i][j],end=" ")
#     print()
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
for i in range(0,2*q_num,2):
    qx,qy=q_lst[i],q_lst[i+1]
    arr[qx][qy]=-1
    for d in range(8):
        x,y=qx,qy
        while True:
            x=x+dx[d]
            y=y+dy[d]
            if not  in_range(x,y) or arr[x][y]==-1:
                break
            arr[x][y]=1

result=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i][j]==0:
            result+=1
print(result)




