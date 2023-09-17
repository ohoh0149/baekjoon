def get_s(s):
    if s[0].isalpha() and s[1].isalpha():
        return s[0].lower()+s[1].lower()
    else:
        return False

dic1=dict()
dic2=dict()
def solution(str1, str2):
    answer = 0

    for i in range(len(str1)-1):

        s=get_s(str1[i:i+2])
        if not s:
            continue
        if s in dic1:
            dic1[s]+=1
        else:
            dic1[s]=1
    for i in range(len(str2)-1):

        s=get_s(str2[i:i+2])
        if not s:
            continue
        if s in dic2:
            dic2[s]+=1
        else:
            dic2[s]=1


    inter_dic=dict()

    
    for key in dic1.keys():
        if key in dic2:
            inter_dic[key]=min(dic1[key],dic2[key])

    
    for key in dic1.keys():
        if key in dic2:
            dic2[key]+=dic1[key]
        else:
            dic2[key]=dic1[key]
    a=0
    b=0
    for key in inter_dic.keys():
        a+=inter_dic[key]
        dic2[key]-=inter_dic[key]
    for key in dic2.keys():
        b+=dic2[key]
    if a==0 and b==0:
        return 65536
    return int((a/b)*65536)
    