def cal(alp1,alp2):
    m=abs(ord(alp1)-ord(alp2))
    if m>13:
        m=26-m

    return m

result=0
name_lst=[]
lst=[]
n=0
def dfs(cur,count):
    #print(cur,count)
    global result

    if count>=result:
        return

    l,r=-1,-1
    ll,rr=0,0

    for i in range(1,n+1):
        if lst[(cur+i)%n]!=name_lst[(cur+i)%n]:
            #print(lst[(cur+i)%n],name_lst[(cur+i)%n])
            r=(cur+i)%n
            rr=i
            break
    for i in range(1,n+1):
        if lst[(cur-i+n)%n]!=name_lst[(cur-i+n)%n]:
            l=(cur-i+n)%n
            ll=i

            break
    #종료 조건
    if l==-1:
        
        result=min(result,count)

        return
    
    
    temp_lst=[l,r]
    temp_lst2=[ll,rr]
    for idx,j in enumerate(temp_lst):
        temp=count+cal(lst[j],name_lst[j])+temp_lst2[idx]
        ori=lst[j]
        lst[j]=name_lst[j]
        dfs(j,temp)
        lst[j]=ori

    return
    



def solution(name):
    global result
    global name_lst
    global lst
    global n
    result=1e9

    name_lst=list(name)
    n=len(name_lst)

    lst=["A"]*len(name_lst)
    
    count=cal(lst[0],name_lst[0])
    lst[0]=name_lst[0]
    dfs(0,count)


    return result