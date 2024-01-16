def dfs(k,num):
    global answer
    if k==n:
        if tar==num:
            answer+=1
        return
    dfs(k+1,num+nums[k])
    dfs(k+1,num-nums[k])
    
nums=[]
tar=0
n=0
answer=0
def solution(numbers, target):
    global n,nums,tar,answer
    nums=numbers
    tar=target
    n=len(numbers)
    dfs(0,0)
    return answer