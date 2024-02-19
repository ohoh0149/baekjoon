def change(n,k):
    s=""
    while n>0:
        s=str(n%k)+s
        n//=k
    return s

def is_prime(num):
    if num==1:
        return False
    
    for i in range(2,int(pow(num,0.5))+1):
        if num%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    s=change(n,k)
    s="0"+s+"0"
    l=len(s)
    s+="x"
    val=""
    for i,a in enumerate(s):
        if i==l:
            break
        if a!="0":
            val+=a
            continue
        if s[i+1]!='0':
            val+=a
    #print(val)
    
    lst=[]
    for i,a in enumerate(val):
        if a=="0":
            lst.append(i)
    #print(lst)
    
    t=len(lst)
    for i in range(t-1):
        temp=int(val[lst[i]+1:lst[i+1]])
        #print("temp",temp)
        if is_prime(temp):
            answer+=1
            
            
        
    return answer