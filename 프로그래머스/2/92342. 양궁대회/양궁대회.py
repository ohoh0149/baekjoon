cur_lst=[0]*11
info_lst=[]

def get_result():
    lion=0
    apeach=0
    min_idx=-1
    count=0
    for i in range(11):
        if cur_lst[i]>0:
            min_idx=i
            count=cur_lst[i]
        if cur_lst[10-i]==info_lst[10-i]==0:
            continue
        if cur_lst[10-i]>info_lst[10-i]:
            lion+=i
        else:
            apeach+=i
    return lion-apeach,min_idx,count

# result=-1e9
# answer=[]
# def dfs(k,left):
#     global cur_lst,result,answer
#     if left<0:
#         return
    
#     if k==11:
#         if left==0:
#             temp=get_result()
#             if temp>0 and temp>result:
#                 answer=cur_lst.copy()
#                 result=temp
                
                
#         return
    
#     #점수획득
#     if left>info_lst[10-k]:
#         cur_lst[10-k]=info_lst[10-k]+1
#         dfs(k+1,left-info_lst[10-k]-1)
#         cur_lst[10-k]=0
    
#     #점수획득x
#     dfs(k+1,left)
    
    
result=-1e9
r1,r2,r3=-1,-1,-1
answer=[]
def dfs(k,left):
    global result,cur_lst,answer,r1,r2,r3
    if left<0:
        return 
    if k==11:
        t1,t2,t3=get_result()

        if t1>0 and (t1,t2,t3)>=(r1,r2,r3):

            answer=cur_lst.copy()
            answer[10]=left

            r1,r2,r3=t1,t2,t3
            #print(result,left,cur_lst)
        return 
    
    #점수획득
    if left>info_lst[k]:
        cur_lst[k]=info_lst[k]+1
        dfs(k+1,left-info_lst[k]-1)
        cur_lst[k]=0
    
    #점수획득x
    dfs(k+1,left)
    
    
    
def solution(n, info):
    global info_lst,answer
    info_lst=info
    
    dfs(0,n)
    #print(result)
    if not answer:
        return [-1]

    return answer