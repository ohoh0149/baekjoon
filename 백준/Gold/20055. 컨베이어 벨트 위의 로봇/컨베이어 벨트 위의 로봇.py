from collections import deque


def add_robot():
    global r_lst
    for i in range(n - 2, -1, -1):
        if r_lst[i] == 0:
            continue
        elif r_lst[i] == 1:
            if i == n - 2:
                r_lst[i] = 0
            else:
                r_lst[i] = 0
                r_lst[i + 1] = 1


def move_robot():
    global r_lst
    global A
    for i in range(n - 2, -1, -1):
        if r_lst[i] == 0:
            continue
        elif r_lst[i] == 1:
            if A[i+1]>0 and r_lst[i+1]==0:
                A[i+1]-=1
                if i == n - 2:
                    r_lst[i] = 0
                else:
                    r_lst[i] = 0
                    r_lst[i + 1] = 1


n,k=map(int,input().split())
lst=list(map(int,input().split()))

A=deque(lst)

r_lst=[0]*n


result=0
while True:
    result+=1
    A.appendleft(A.pop())
    add_robot()
    move_robot()
    if A[0]>0:
        r_lst[0]=1
        A[0]-=1
    count=0
    for a in A:
        if a==0:
            count+=1
    if count>=k:
        break
print(result)



