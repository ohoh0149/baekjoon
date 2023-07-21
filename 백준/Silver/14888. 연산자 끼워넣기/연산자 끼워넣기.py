
def cal(val1,val2,d):
    if d==0:
        result=val1+val2
    if d==1:
        result=val1-val2
    if d==2:
        result=val1*val2
    if d==3:
        if val1>=0:
            result=val1//val2
        else:
            result=-(-val1//val2)
    return result


def dfs(k,result):
    global max_result
    global min_result
    global b_lst
    if k==n-1:
        max_result=max(result,max_result)
        min_result=min(result,min_result)
        return
    for i in range(4):
        if b_lst[i]>0:
            b_lst[i]-=1
            dfs(k+1,cal(result,a_lst[k+1],i))
            b_lst[i]+=1
    return


n=int(input())
a_lst=list(map(int,input().split()))

b_lst=list(map(int,input().split()))

max_result=-1e9
min_result=1e9
dfs(0,a_lst[0])
print(max_result)
print(min_result)



