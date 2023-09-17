def make_time(hour,minute):
    a=minute//60
    b=minute%60
    return (hour+a)*100+b

import copy
def check(int_time):
    global time_lst
    
    time_lst_idx=0
    for i in range(n):
        hour=9
        minute=t*(i)
        bus_time=make_time(hour,minute)
        
        for j in range(m):
            if time_lst_idx==time_len:
                return True
            if time_lst[time_lst_idx]>int_time:
                return True
            if time_lst[time_lst_idx]<=bus_time:
                time_lst_idx+=1
            else:
                break                

    return False
        
        
        
        
        
        
        
        
        
        
    

    
    



def stoi(s):
    ns=s[:2]+s[3:]
    return int(ns)

def itos(num):
    s=str(num)
    if num<10:
        s="000"+s
    elif num<100:
        s="00"+s
    elif num<1000:
        s="0"+s
    ns=s[:2]+":"+s[2:]
    return ns
time_lst=[]
n=0
t=0
time_len=0
def solution(aaa, bbb, ccc, timetable):
    global time_lst
    global n,t,m
    global time_len
    time_len=len(timetable)
    n=aaa
    t=bbb
    m=ccc
    for s in timetable:
        time_lst.append(stoi(s))
    time_lst.sort()


    #a=9+(n-1)*t//60
    #b=((n-1)*t)%60
    last_time=make_time(9,(n-1)*t)



    result=0


    
    #for int_time in range(last_time,-1,-1):
    int_time=last_time
    while int_time>=0:
        if int_time%100==99:
            int_time-=40
        if check(int_time):
            result=int_time
            break
        
        int_time-=1
    
    
    
    
    return itos(result)