n=int(input())
dic=dict()
for _ in range(n):
    x,y1,y2=input().split()
    dic[x]=[y1,y2]


def preorder(alp):
    if alp==".":
        return
    print(alp,end="")
    preorder(dic[alp][0])
    preorder(dic[alp][1])

def inorder(alp):
    if alp==".":
        return
    inorder(dic[alp][0])
    print(alp,end="")
    inorder(dic[alp][1])

def postorder(alp):
    if alp==".":
        return
    postorder(dic[alp][0])
    postorder(dic[alp][1])
    print(alp,end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")