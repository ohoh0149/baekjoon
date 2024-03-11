result=1e9


def get_result(reqs):
    #cur_lst
    cur_result=0

    arr=[[]]
    for i in range(1,k+1):
        a=cur_lst[i]
        arr.append([0]*(a+1))

    cur_time=0
    for a,b,c in reqs:
        find_flag=False
        for i in range(1,cur_lst[c]+1):
            if arr[c][i]==0 or arr[c][i]<=a:
                arr[c][i]=a+b
                find_flag=True
                break
        if not find_flag:
            min_val=min(arr[c][1:])
            min_idx=arr[c].index(min_val)
            cur_result+=(min_val-a)
            arr[c][min_idx]+=b

            
    return cur_result
            
        
                
            

    



def dfs(l,rest,reqs):
    global cur_lst,count,result
    if l==k:
        if rest==0:
            result=min(result,get_result(reqs))
        return
    if rest<=0:
        return
    for i in range(1,rest+1):
        cur_lst[l+1]=i
        dfs(l+1,rest-i,reqs)
        cur_lst[l+1]=0
        

cur_lst=[]
k=0
n=0
def solution(a, b, reqs):
    global k,n,cur_lst,result
    k=a
    n=b
    cur_lst=[0]*(k+1)
    answer = 0
    dfs(0,n,reqs)
    answer=result

    return answer