from collections import deque

n,k= map(int,input().split())
q=deque(map(int,input().split()))

robot=deque()
result=0
while True:
    result+=1
    #print(result)
    #print(q)
    # if result==5:
    #     break

    #1
    q.appendleft(q.pop())
    for i in range(len(robot)):
        robot[i]+=1
    if len(robot)>0 and robot[0]==n-1:
        robot.popleft()
    #2
    before_robot=0
    length=len(robot)
    for i in range(length):
        if q[robot[i]+1]>=1 and before_robot!=robot[i]+1:
            robot[i]+=1
            if robot[i]==n-1:
                q[robot[i]]-=1
                before_robot=0
                continue
            q[robot[i]]-=1
        before_robot=robot[i]

    if len(robot)>0 and robot[0]==n-1:
        robot.popleft()
    if q[0]>0:
        robot.append(0)
        q[0]-=1
    if q.count(0)>=k:
        break
    
print(result)




