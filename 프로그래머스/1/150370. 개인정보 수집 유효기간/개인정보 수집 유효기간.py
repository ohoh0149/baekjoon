def solution(today, terms, privacies):
    answer = []
    
    def get_3(day):
        return int(day[:4]),int(day[5:7]),int(day[8:])
    
    
    def add_day(ymd,m):
        year,month,day=get_3(ymd)
        am=month+int(m)
        if am%12==0:
            ay=year+(am//12)-1
            am=12
        else:
            ay=year+am//12
            am=am%12
        return ay,am,int(day)
    
    
    dic=dict()
    for term in terms:
        dic[term[0]]=int(term[2:])

    aa=get_3(today)
    for idx,privacy in enumerate(privacies):
        temp=add_day(privacy[:-2],dic[privacy[-1]])

        if temp<=aa:
            answer.append(idx+1)
            
        
        

    
    return answer