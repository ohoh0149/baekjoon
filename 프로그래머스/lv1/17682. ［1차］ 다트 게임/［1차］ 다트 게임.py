dic=dict()
dic["S"]=1
dic["D"]=2
dic["T"]=3

def get_where(idx,idx_lst):
    if idx_lst[0]<idx<idx_lst[1]:
        return 1
    elif idx_lst[1]<idx<idx_lst[2]:
        return 2
    else:
        return 3
    

def solution(dartResult):
    last_idx=0
    score_lst=[0]
    l=len(dartResult)
    cur_idx=0
    for idx,s in enumerate(dartResult):
        if s in ["S","D","T"]:
            #print(dartResult[last_idx:idx])
            if dartResult[idx-1]=="0":

                if idx>=2 and  dartResult[idx-2]=="1":
                    score_lst.append(10**dic[s])
                else:
                    score_lst.append(0)
            else:
                score_lst.append(int(dartResult[idx-1])**dic[s])
            cur_idx+=1
            if idx!=l-1:
                if dartResult[idx+1] =="*":
                    score_lst[cur_idx-1]*=2
                    score_lst[cur_idx]*=2
                elif dartResult[idx+1]=="#":
                    score_lst[cur_idx]*=-1
    
                    
                    

    print(score_lst)
    return sum(score_lst)

            
    
    
#     idx_lst=[]
#     #print(dir(""))
#     for idx,s in enumerate(dartResult):
#         if s.isdigit():
#             idx_lst.append(idx)

#     score_lst=[0]*4
#     s1=dartResult[idx_lst[0]:idx_lst[1]]
#     s2=dartResult[idx_lst[1]:idx_lst[2]]
#     s3=dartResult[idx_lst[2]:]
#     s_lst=[s1,s2,s3]

#     for j,st in enumerate(s_lst):
#         for idx,s in enumerate(st):
#             if s =="S" or s=="D" or s=="T":
#                 a=int(st[:idx])
#                 score_lst[j+1]=a**dic[s]
#                 break

    
#     for idx,s in enumerate(dartResult):
#         if s=="*" or s=="#":
#             l=get_where(idx,idx_lst)
#             if s=="*":
#                 score_lst[l-1]*=2
#                 score_lst[l]*=2
#             else:
#                 score_lst[l]*=-1
#     print(score_lst)
#     return sum(score_lst)
     