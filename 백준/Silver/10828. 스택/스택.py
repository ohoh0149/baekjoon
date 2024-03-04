import sys
input=sys.stdin.readline
n=int(input())
stack=[]
count=0
for _ in range(n):
    inp=input().split()
    s=inp[0]

    if s=="push":
        num=int(inp[1])
        stack.append(num)
        count+=1
    elif s=="pop":
        if count!=0:
            print(stack.pop())
            count-=1
        else:
            print(-1)
    elif s=="size":
        print(count)
    elif s=="empty":
        if count==0:
            print(1)
        else:
            print(0)
    elif s=="top":
        if count!=0:
            print(stack[-1])
        else:
            print(-1)