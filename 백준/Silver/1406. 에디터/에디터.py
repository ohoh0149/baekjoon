import sys

inp=input()
input=sys.stdin.readline


head=[0,0,0]
ptr=head
for s in inp:
    node=[0,s,0]
    ptr[2]=node
    node[0]=ptr
    ptr=node

def print_all(node):
    node=node[2]
    if node==0:
        return
    while True:
        print(node[1],end="")
        node=node[2]
        if node==0:
            break
    print()

m=int(input())
for _ in range(m):
    # print_all(head)
    # print(ptr[1])

    query=input().split()
    if query[0]=="L":
        if ptr[0]!=0:
            ptr=ptr[0]
    elif query[0]=="D":
        if ptr[2]!=0:
            ptr=ptr[2]
    elif query[0]=="B":
        if ptr[0]!=0:
            ptr[0][2]=ptr[2]
            if ptr[2]!=0:
                ptr[2][0]=ptr[0]
            ptr=ptr[0]
    else:
        b=query[1]
        node=[0,b,0]
        node[2]=ptr[2]
        if ptr[2]!=0:
            ptr[2][0]=node
        ptr[2]=node
        node[0]=ptr
        ptr=node

print_all(head)

