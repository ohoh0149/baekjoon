dic=dict()
temp_lst=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]



def find_w(msg):
    global answer_lst
    l=len(msg)
    
    for i in range(2,l+1):
        if msg[:i] not in dic:
            #print(dic[msg[:i-1]])
            answer_lst.append(dic[msg[:i-1]])
            return msg[:i-1]
    
    answer_lst.append(dic[msg])
    return msg
            
    
#     for i in range(l-1,0,-1):
#         cur_msg=msg[:i]
#         if msg[:i] in dic:
#             return cur_msg
    

answer_lst=[]
def solution(msg):
    global dic
    for idx,s in enumerate(temp_lst):
        dic[s]=idx+1
    
    count=27


    while msg:
        w=find_w(msg)
        print(w)
        
        l=len(w)
        if l==len(msg):
            dic[w]=count
            count+=1
            msg=""
        else:
            dic[w+msg[l]]=count
            count+=1
            msg=msg[l:]

        


    

        
                
            

    
    return answer_lst