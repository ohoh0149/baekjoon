from collections import deque
q1=deque()
q2=deque()
q3=deque()
q4=deque()
q_arr=[q1,q2,q3,q4]
for i in range(4):
    str=input()
    for j in range(8):
        q_arr[i].append(int(str[j]))
k=int(input())
turn_arr=[]
for i in range(k):
    num,d=map(int,input().split())
    num-=1
    turn_arr.append((num,d))
#print(q_arr)
# print(turn_arr)


def turn_left(q):
    q.append(q.popleft())
    return 0
def turn_right(q):
    q.appendleft(q.pop())
def turn(q,d):
    if d==-1:
        q.append(q.popleft())
    elif d==1:
        q.appendleft(q.pop())


def rec_turn(num,d):
    #print(num)
    if num>3 or num<0 or visited[num]==1:
        return False
    else:
        cur_6=q_arr[num][6]
        cur_2=q_arr[num][2]
        visited[num]=1
        turn(q_arr[num],d)
        #print("turn",num,d)
        
        if num-1>=0 and cur_6!=q_arr[num-1][2]:
            rec_turn(num-1,-d)
        if num+1<4 and cur_2!=q_arr[num+1][6]:
            rec_turn(num+1,-d)
        return True





for i in range(k):
    #q=1,2,3,4 d=-1,1
    q_num,d=turn_arr[i]
    visited=[0,0,0,0]
    rec_turn(q_num,d)
    
#print(q_arr)
result=0
for i in range(4):
    result+=(2**i)*q_arr[i][0]
print(result)

    

    