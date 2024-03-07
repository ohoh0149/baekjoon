from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m

n,m=map(int,input().split())
arr=[list(map(int,list(input()))) for _ in range(n)]



result=0

not_fill_arr=[[False]*m for _ in range(n)]
while True:
    fill_flag=False
    for i in range(n):
        for j in range(m):
            if not_fill_arr[i][j]:
                continue
            #같은 높이 좌표들, 주변 최대 높이
            visited=[[False]*m for _ in range(n)]
            pos_lst=[(i,j)]
            min_h=1e9
            q=deque()
            q.append((i,j))
            visited[i][j]=True

            impossible_flag=False
            while q:
                x,y=q.popleft()

                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if not in_range(nx,ny):
                        impossible_flag=True
                        break
                    if visited[nx][ny]:
                        continue

                    if arr[nx][ny]==arr[x][y]:
                        q.append((nx,ny))
                        visited[nx][ny]=True
                        pos_lst.append((nx,ny))
                    elif arr[nx][ny]>arr[x][y]:
                        min_h=min(min_h,arr[nx][ny])
                    else:
                        impossible_flag=True
                        break


                if impossible_flag:
                    break


            #가능한 경우 물채우기
            if not impossible_flag:
                fill_flag=True
                for x,y in pos_lst:
                    result+=min_h-arr[x][y]
                    arr[x][y]=min_h
            #불가능한 경우 못채운다고 표시
            else:
                for x,y in pos_lst:
                    not_fill_arr[x][y]=True


    if not fill_flag:
        break


def print_arr(arr):
    for i in range(n):
        print(arr[i])
    print()
# print_arr(not_fill_arr)
# print_arr(arr)
print(result)