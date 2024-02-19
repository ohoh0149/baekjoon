from collections import defaultdict
def cal(time1,time2):
    h1,m1=int(time1[:2]),int(time1[3:])
    h2,m2=int(time2[:2]),int(time2[3:])
    
    if m1>m2:
        h2-=1
        m2+=60
    return (h2-h1)*60+m2-m1


def get_result(num,dic2,fees):
    if dic2[num]<=fees[0]:
        return fees[1]

    val=dic2[num]-fees[0]
    if val%fees[2]==0:
        return fees[1]+(val//fees[2])*fees[3]
    else:
        return fees[1]+(val//fees[2]+1)*fees[3]
    
    

def solution(fees, records):
    
    answer = []
    dic1=defaultdict(int)
    dic2=defaultdict(int)
    name_set=set()
    for record in records:
        time,num,inout=record.split()
        name_set.add(num)
        if inout=="IN":
            dic1[num]=time
        else:
            m=cal(dic1[num],time)
            del dic1[num]
            dic2[num]+=m
    for key,value in dic1.items():
        dic2[key]+=cal(value,"23:59")
        
    lst=list(name_set)
    lst.sort()
    
    
    
    
    for num in lst:
        res=get_result(num,dic2,fees)
        answer.append(res)





    

    
    return answer