import heapq,sys
from collections import deque

input=sys.stdin.readline

T=int(input())
for _ in range(T):
    p=input()
    n=int(input())
    st=input()
    st=st[1:-2]
    lst=[]
    if st:
        lst=list(st.split(","))
        lst=list(map(int,lst))

    q=deque(lst)
    r=-1
    error_flag=False
    for s in p:
        if s=="R":
            r=-1*r
        elif s=="D":
            if not q:
                error_flag=True
                break
            if r==-1:
                q.popleft()
            else:
                q.pop()

    if error_flag:
        print("error")
    else:
        if r==1:
            q.reverse()

        print("[",end="")
        temp_lst=list(q)
        if len(temp_lst)>1:
            for temp in temp_lst[:-1]:
                print(str(temp)+",",end="")
            print(q[-1],end="")
        elif len(temp_lst)==1:
            print(q[-1],end="")
        print("]")

