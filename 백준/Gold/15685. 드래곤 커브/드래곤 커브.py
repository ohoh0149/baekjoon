import copy
def turn_clock_dot(ax,ay,cx,cy):
    rx=cx+cy-ay
    ry=cy-cx+ax
    return rx,ry

def turn_clock_dot_arr(cx,cy,arr):
    global temp_cx,temp_cy
    ret_arr=copy.deepcopy(arr)
    count=0
    for x,y in arr:
        rx,ry=turn_clock_dot(x,y,cx,cy)
        if count==0:
            temp_cx,temp_cy=rx,ry
            count+=1
        if (rx,ry) not in ret_arr:
            
            ret_arr.append((rx,ry))
    
    return ret_arr

#turn_clock_dot_arr(4,3,[(5,1),(6,4)])



graph=[[0]*101 for i in range(101)]

dx=[1,0,-1,0]
dy=[0,-1,0,1]
n=int(input())
temp_cx=0
temp_cy=0
for i in range(n):
    x,y,d,g=map(int,input().split())
    temp_cx,temp_cy=x+dx[d],y+dy[d]
    temp_dot_list=[(x,y),(temp_cx,temp_cy)]
    for j in range(g):
        #print("i,j,tempcx,tempcy",i,j,temp_cx,temp_cy)
        temp_dot_list=turn_clock_dot_arr(temp_cx,temp_cy,temp_dot_list)
    
    for a,b in temp_dot_list:
        graph[a][b]=1


result=0

for i in range(100):
    for j in range(100):
        if graph[i][j]==1 and graph[i+1][j]==1 and graph[i][j+1]==1 and graph[i+1][j+1]==1:
            result+=1
print(result)

