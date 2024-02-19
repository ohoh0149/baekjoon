def solution(id_list, report, k):
    answer = [0]*len(id_list)
    dic1=dict()
    count_dic=dict()
    for i in id_list:
        dic1[i]=set()
        count_dic[i]=0

    
    for r in report:
        a,b=r.split()
        dic1[a].add(b)
    
    for _,s in dic1.items():

        for name in s:
            count_dic[name]+=1

    
    for key,v in count_dic.items():
        if v>=k:
            for idx,user in enumerate(id_list):
                if key in dic1[user]:
                    answer[idx]+=1
                    
        
    
        
    return answer