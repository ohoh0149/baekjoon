import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
graph=[[0]*(n+1) for i in range(n+1)]
num_apple=int(input())
for i in range(num_apple):
    a,b=map(int,input().split())
    #사과
    graph[a][b]=-1
l=int(input())
direction=deque()
for i in range(l):
    x,c=input().split()
    x=int(x)
    direction.append((x,c))
#print(graph,direction)
snake=deque()

def turn_right(dir):
    dir=(dir+1)%4
    return dir
def turn_left(dir):
    dir=(dir+4-1)%4
    return dir
def move(a,b,dir):
    global now_row,now_col
    now_row=a+dx[dir]
    now_col=b+dy[dir]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
now_row=1
now_col=1
graph[1][1]=1
tail_row=1
tail_col=1
length=1
next_tail_row=1
next_tail_col=1
count=1
now_dir=0
snake.append((1,1))
while 1:
    #print(now_row,now_col)
    #print(now_row,now_col)
    #print(graph)
    if len(direction)!=0 and direction[0][0]==count-1:
        temp,dir=direction.popleft()
        if dir=='L':
            now_dir=turn_left(now_dir)
        elif dir=='D':
            now_dir=turn_right(now_dir)
    move(now_row,now_col,now_dir)

    if length==1:
        next_tail_row=now_row
        next_tail_col=now_col
    if now_row>n or now_row<1 or now_col>n or now_col<1 or graph[now_row][now_col]==1:
        break
    if graph[now_row][now_col]==-1:# 만약 사과위치라면
        snake.append((now_row,now_col))
        graph[now_row][now_col]=1
    elif graph[now_row][now_col]==0:
        snake.append((now_row,now_col))
        tail_row,tail_col=snake.popleft()
        graph[tail_row][tail_col]=0
        graph[now_row][now_col]=1
    count+=1
print(count)
    
    