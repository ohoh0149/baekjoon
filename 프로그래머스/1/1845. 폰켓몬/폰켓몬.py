def solution(nums):
    answer = 0
    dic=dict()
    for n in nums:
        dic[n]=0
    for n in nums:
        dic[n]+=1
    l=len(dic)
    N=len(nums)
    answer=min(N//2,l)

    
    return answer