def remove_cache(name,time):
    global cache
    minidx=0
    minval=1e9
    for idx, a in enumerate(cache):
        if a[1]<minval:
            minval=a[1]
            minidx=idx
    
    cache[minidx]=[name,time]

def check_s(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        if s1[i].upper()!=s2[i].upper():
            return False
    
    return True

def check_isin(name):
    for idx,a in enumerate(cache):
        if check_s(name,a[0]):
            return idx
    
    return -1
        

        

cache=[]
def solution(cacheSize, cities):
    global cache
    answer = 0
    for turn,name in enumerate(cities):    
        flag=check_isin(name)
        if flag!=-1:
            cache[flag][1]=turn
            answer+=1
        else:
            answer+=5
            if len(cache)<cacheSize:
                cache.append([name,turn])
            elif cacheSize!=0:
                remove_cache(name,turn)
            
                
            
        
        
    return answer