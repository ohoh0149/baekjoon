def cal(time,t):
    h,m,s=time
    s=s+t
    if s>=60000:
        m+=1
        s-=60000
        if m>=60:
            h+=1
            m-=60
    elif s<0:
        m-=1
        s+=60000
        if m<0:
            m+=60
            h-=1
    return (h,m,s)
    
    


# def change_time(num):
#     if num%100000>=60000:
#         num-=60000
#         num+=100000
#     if num%10000000>=6000000:
#         num-=60000
#         num+=10000000
#     return num

def solution(lines):
    answer = 0
    lst=[]
    
    


    for s in lines:

        h=int(s[11:11+2])
        m=int(s[14:14+2])
        sec=int(s[17:17+2]+s[20:20+3])
        t=int(float(s[24:-1])*1000)
        lst.append(((h,m,sec),t))
        
    for start_time,_ in lst:

        end_time=cal(start_time,1000-1)
        #print("start",start_time,end_time)
        count=0
        for right_time,t in lst:
            left_time=cal(right_time,-t+1)

            if left_time<=end_time<=right_time or left_time<=start_time<=right_time or start_time<=left_time<=right_time<=end_time:
                #print(left_time,right_time)
                count+=1
        answer=max(count,answer)
    
    
    return answer
        
        
#     for start, _ in lst:
#         count=0
#         end=start+1000-1
#         end=change_time(end)
        
        
#         print("start,end",start,end)
#         for r,t in lst:
#             #l=r-t+1
#             #r=l+t-1
#             #l=change_time(l)

#             if  (r<=change_time(start+t-1)and start<=r) or change_time(start+t-1)<=r<=change_time(end+t-1) or start<=r<=end or (r<=change_time(end+t-1 )and end<=r):
#                 print("in",r,t)
#                 count+=1
#             else:
#                 print("out",r,t)
#             # if r>end+3001:
#             #     break
#         print(count)
#         answer=max(count,answer)
        
    return answer