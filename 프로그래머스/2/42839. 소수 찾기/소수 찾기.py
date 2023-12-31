import math

from itertools import permutations
def isPrime(num):
    if num in [0,1]:
        return False
    a=math.sqrt(num)
    
    for i in range(2,int(a)+1):
        if num%i==0:
            return False
    return True
        
    
    

def solution(numbers):
    answer = 0
    lst=list(numbers)
    s=set()
    for i in range(1,len(lst)+1):
        per_lst=list(set(permutations(lst,i)))
        
        for per in per_lst:
            a="".join(per)
            s.add(int(a))
    
    #print(s)
    for num in s:
        if isPrime(num):
            #print(num)
            answer+=1
    
    return answer