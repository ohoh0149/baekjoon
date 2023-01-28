n=int(input())
t=[0]
p=[0]

for i in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)

#print(t,p)
result=0

def cal(day,sum,before_day):
    
    global result
    if day>n:
        if before_day+t[before_day]==n+1:
            sum+=p[before_day]
        if sum>result:
            result=sum
         #   print("hhhh",day,sum,before_day)
            return
    else:
        sum+=p[before_day]
        #print(day,sum,before_day)
        if day+t[day]>=n+1:
            cal(day+t[day],sum,day)
        else:
            for i in range(day+t[day],n+1):
                cal(i,sum,day)
            




for i in range(1,n+1):
    cal(i,0,0)
print(result)





