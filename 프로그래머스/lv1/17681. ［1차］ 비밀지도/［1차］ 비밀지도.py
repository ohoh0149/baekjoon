from collections import deque
def change(num):
    q=deque()
    while num>0:
        q.appendleft(num%2)
        num//=2
    
    while len(q)<l:
        q.appendleft(0)
    return q
    
        

l=0
def solution(n, arr1, arr2):
    global l
    l=n
    ar1=[]
    ar2=[]
    for num in arr1:
        ar1.append(change(num))
    for num in arr2:
        ar2.append(change(num))
    
    result_arr=[]
    for i in range(n):
        s=""
        for j in range(n):
            if ar1[i][j]==0 and ar2[i][j]==0:
                s+=" "
            else:
                s+="#"
        result_arr.append(s)
        
    return result_arr