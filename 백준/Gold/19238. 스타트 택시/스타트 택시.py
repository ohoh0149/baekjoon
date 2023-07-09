from collections import deque
def in_range(x,y):
    if 1<=x<=n and 1<=y<=n:
        return True
    else:
        return False


#최단거리 승객 찾고 ( 거리 0도 가능), 현재 택시 위치 이동, 연료 감소 연료 0이하면 실패, 목적지 좌표 반환
def find_passenger():
    global sx,sy,fuel
    global dic
    rx,ry=-1,-1
    #현재 위치에 승객 있는 경우
    if (sx,sy) in dic.keys():
        rx,ry=dic[(sx,sy)]
        del dic[(sx,sy)]
        return rx,ry

    pas_len=1e9
    pas_list=[]

    q=deque()
    visited=[[-1]*(n+1) for _ in range(n+1)]
    q.append((sx,sy))
    visited[sx][sy]=0
    while q:
        x,y=q.popleft()
        #print(x,y)
        if visited[x][y]>=pas_len:
            break
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            #승객 발견한 경우
            if in_range(nx,ny) and visited[nx][ny]==-1 and  (nx,ny) in dic.keys() and visited[x][y]<=pas_len-1:
                visited[nx][ny]=visited[x][y]+1
                pas_len=visited[x][y]+1
                #print("pas_list append nx,ny",nx,ny)
                pas_list.append((nx,ny))
                #print("pas_list:",pas_list)
                #print("fuel-=",visited[x][y]+1)

                #fuel-=(visited[x][y]+1)
                #print("fuel = ", fuel)
                if fuel-(visited[x][y]+1)<=0:
                    #print("승객 발견했으나 연료 부족으로 return -1 -1")
                    return rx,ry
                # sx,sy=nx,ny
                # rx, ry = dic[(sx, sy)]
                # del dic[(sx, sy)]
                # return rx, ry
            if in_range(nx,ny) and arr[nx][ny]==0 and visited[nx][ny]==-1:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))

    if len(pas_list)==0:
        #print("승객 발견x")
        return -1,-1
    pas_list.sort()
    sx=pas_list[0][0]
    sy=pas_list[0][1]
    fuel-=pas_len
    #print("연료:",fuel)
    #print("현재 위치",sx,sy)
    rx,ry=dic[(sx,sy)]
    del dic[(sx,sy)]
    return rx,ry

#def find_passenger():


#목적지로 택시 위치 이동, 연료 감소 시켜서 0보다 작으면 실패 (현재 승객의 이동 거리*2)만큼 연료 증가
def go_final(rx,ry):
    global sx,sy,fuel
    q = deque()
    visited = [[-1] * (n + 1) for _ in range(n + 1)]
    q.append((sx, sy))
    visited[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 도착지 발견한 경우
            if rx==nx and  ry ==ny:
                fuel -= (visited[x][y] + 1)
                if fuel < 0 :
                    #print("도착지 발견 했으나 연료 부족으로 return False, fuel:",fuel)
                    return False
                sx, sy = nx, ny
                #print("연료 증가 :",(visited[x][y]+1)*2)
                fuel+=(visited[x][y]+1)*2
                #print("fuel:",fuel)
                return True
            if in_range(nx, ny) and arr[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    #도착지 발견 못함
    #print("도착지 발견 못함!")
    return False

dx=[-1,0,0,1]
dy=[0,-1,1,0]

n,m,fuel=map(int,input().split())

arr=[[0]*(n+1)]
for _ in range(n):
    arr.append(([0]+list(map(int,input().split()))))
sx,sy=map(int,input().split())
dic={}
for _ in range(m):
    a,b,c,d=map(int,input().split())
    dic[(a,b)]=(c,d)
#
# print(find_passenger())
# sx,sy=1,6
# fuel+=6
# print(find_passenger())
result=-1
while True:
    x,y=find_passenger()
    if x==-1:
        break
    if not go_final(x,y):
        break
    if len(dic)==0:
        result=fuel
        break
print(result)