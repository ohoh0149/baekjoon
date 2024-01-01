from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    
    l=0
    r=len(people)-1

    while l<r:
        if people[r]+people[l]>limit:
            answer+=1
            r-=1
        else:
            r-=1
            l+=1
            answer+=1
    
    if l==r:
        answer+=1
            
            
    return answer

