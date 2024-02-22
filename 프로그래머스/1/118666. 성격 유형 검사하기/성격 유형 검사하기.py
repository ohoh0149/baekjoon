from collections import defaultdict

def solution(survey, choices):
    answer = ''
    point_lst=[0,3,2,1,0,1,2,3]
    dic=defaultdict(int)
    for c,num in zip(survey,choices):
        #print(c,num)
        point=point_lst[num]
        if num<4:
            dic[c[0]]+=point
        else:
            dic[c[1]]+=point
    #print(dic)
    #RT  CF  JM  AN
    if dic['R']>=dic['T']:
        answer+='R'
    else:
        answer+="T"
        
    if dic['C']>=dic['F']:
        answer+='C'
    else:
        answer+="F"
    if dic['J']>=dic['M']:
        answer+='J'
    else:
        answer+="M"
    if dic['A']>=dic['N']:
        answer+='A'
    else:
        answer+="N"
    
            
    
    return answer