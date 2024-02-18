def solution(cap, n, deliveries, pickups):
    answer = -1
    p1,p2=-1,-1
    for i in range(n-1,-1,-1):
        if deliveries[i]!=0:
            p1=i
            break
    for i in range(n-1,-1,-1):
        if pickups[i]!=0:
            p2=i
            break
            
    result=0
    while p1>=0 or p2>=0:
        #print(p1,p2)
        result+=2*max(p1,p2)+2
        de=cap
        pi=cap
        while de>=0 and p1>=0:
            if deliveries[p1]==0:
                p1-=1
                continue
            if deliveries[p1]<=de:
                de-=deliveries[p1]
                p1-=1
            else:
                deliveries[p1]-=de
                break
                
        while pi>=0 and p2>=0:

            if pickups[p2]==0:
                p2-=1
                continue
            if pickups[p2]<=pi:
                pi-=pickups[p2]
                p2-=1
            else:
                pickups[p2]-=pi
                break

    return result