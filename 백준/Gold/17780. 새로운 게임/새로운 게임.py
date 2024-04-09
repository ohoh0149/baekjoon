n,k=map(int,input().split())
arr=[[2]*(n+2)]
for _ in range(n):
    arr.append([2]+list(map(int,input().split()))+[2])
arr.append([2]*(n+2))

map_d=[0,1,3,0,2]
m_arr=[[0]*(n+2) for _ in range(n+2)]
for i in range(1,n+1):
    for j in range(1,n+1):
        m_arr[i][j]=[]

def print_arr(arr):
    for i in range(n+2):
        print(arr[i])
    print()

for num in range(1,k+1):
    x,y,d=map(int,input().split())
    d=map_d[d]
    m_arr[x][y].append([num,d])




def find_num_pos(num):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if m_arr[i][j] and m_arr[i][j][0][0]==num:
                return i,j
    return -1,-1

result=0


dx=[-1,0,1,0]
dy=[0,1,0,-1]
end_flag=False
for turn in range(1,1001):
    for num in range(1,k+1):
        x,y=find_num_pos(num)
        if x==-1:
            continue
        d=m_arr[x][y][0][1]
        nx=x+dx[d]
        ny=y+dy[d]
        if arr[nx][ny]==0:
            m_arr[nx][ny].extend(m_arr[x][y])
            m_arr[x][y]=[]
        elif arr[nx][ny]==1:
            m_arr[nx][ny].extend(reversed(m_arr[x][y]))
            m_arr[x][y]=[]
        else:
            m_arr[x][y][0][1]=(d+2)%4
            d=(d+2)%4
            nx=x+dx[d]
            ny=y+dy[d]
            if arr[nx][ny] == 0:
                m_arr[nx][ny].extend(m_arr[x][y])
                m_arr[x][y] = []
            elif arr[nx][ny] == 1:
                m_arr[nx][ny].extend(reversed(m_arr[x][y]))
                m_arr[x][y] = []

        if m_arr[nx][ny] and  len(m_arr[nx][ny])>=4:
            end_flag=True
            result=turn
            break

    if end_flag:
        break

if result==0:
    print(-1)
else:
    print(result)
