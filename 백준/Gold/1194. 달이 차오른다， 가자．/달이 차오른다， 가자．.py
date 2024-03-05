from collections import deque
n,m=map(int,input().split())
arr=[list(input()) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m

dic=dict()
dic["a"]=1
dic["b"]=2
dic["c"]=4
dic["d"]=8
dic["e"]=16
dic["f"]=32
visited=[[[0]*65 for _ in range(m)] for _ in range(n)]

q=deque()
for i in range(n):
    for j in range(m):
        if arr[i][j]=="0":
            arr[i][j]="."
            q.append((i,j,0))
            visited[i][j][0]=1

def check(num1,num2):
    if num1|num2==num1:
        return True
    else:
        return False






while q:
    x,y,c=q.popleft()
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and arr[nx][ny]!="#" and visited[nx][ny][c]==0:
            if arr[nx][ny]==".":
                q.append((nx,ny,c))
                visited[nx][ny][c]=visited[x][y][c]+1
            elif arr[nx][ny]=="1":
                print(visited[x][y][c])
                exit()
            elif arr[nx][ny] in ["a","b","c","d","e","f"]:
                if check(c,dic[arr[nx][ny]]):
                    q.append((nx,ny,c))
                else:
                    new_c=c+dic[arr[nx][ny]]
                    visited[nx][ny][new_c]=visited[x][y][c]+1
                    q.append((nx,ny,new_c))
                visited[nx][ny][c] = visited[x][y][c] + 1
            else:
                cur_alp=arr[nx][ny].lower()
                if check(c,dic[cur_alp]):
                    visited[nx][ny][c]=visited[x][y][c]+1
                    q.append((nx,ny,c))



print(-1)



# a=bin(28)
# b=bin(4)
# print(b)
# for i in range(len(b)-1,-1,-1):
#     if b[i]=="1":
#         print(i)

