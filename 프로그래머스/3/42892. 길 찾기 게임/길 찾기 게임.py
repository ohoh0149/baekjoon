import copy
import sys
sys.setrecursionlimit(10 ** 6)
#node : left, right, n번 노드,x,y

def solution(nodeinfo):
    answer = [[]]
    
    node_lst=[]
    for idx,(x,y) in enumerate(nodeinfo,start=1):

        node_lst.append((idx,x,y))
    node_lst.sort(key=lambda x:(x[2],-x[1]),reverse=True)
    #node_lst n번노드,x,y
    root=[0,0,node_lst.pop(0)]


    def insert_node(par,n,x,y):
        #부모의 x좌표
        if par[2][1]>x:
            if par[0]==0:
                par[0]=[0,0,(n,x,y)]
            else:
                insert_node(par[0],n,x,y)
        else:
            if par[1]==0:
                par[1]=[0,0,(n,x,y)]
            else:
                insert_node(par[1],n,x,y)
        
    for n,x,y in node_lst:
        insert_node(root,n,x,y)
    

    
    lst1=[]
    def preorder(node):
        if node==0:
            return
        lst1.append(node[2][0])
        preorder(node[0])
        preorder(node[1])
        
    
    preorder(root)

    lst2=[]
    def postorder(node):
        if node==0:
            return
        postorder(node[0])
        postorder(node[1])
        lst2.append(node[2][0])

    postorder(root)

        

    return [lst1,lst2]
