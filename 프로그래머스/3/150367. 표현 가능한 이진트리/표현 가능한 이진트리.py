def make_binary(num):
    s=""
    while num>0:
        s=str(num%2)+s
        num//=2
    return s

lst=[]
gb=[]
l=0
def inorder(x):
    global lst
    if not 0<x<=l:
        return 
    inorder(x*2)
    lst[x]=gb.pop(0)
    inorder(x*2+1)

def make_tree(b):
    global lst,gb,l
    gb=list(b)
    l=len(b)
    lst=[0]*(l+1)
    lst[0]=1
    inorder(1)
    return lst

def solution(numbers):
    answer = []
    b_set=set([1,3,7,15,31,63])
    for number in numbers:
        b=make_binary(number)


        while True:
            if len(b) in b_set:
                break
            b="0"+b
        #print(b)
        tree_lst=make_tree(b)
        #print(b)
        #print(tree_lst)
        l=len(b)
        flag=1
        for i in range(1,l+1):
            if tree_lst[i]=='1' and tree_lst[i//2]=='0':
                flag=0
                break
        answer.append(flag)

        
        
        
        

        
    return answer