dic=dict()
dic[10]="A"
dic[11]="B"
dic[12]="C"
dic[13]="D"
dic[14]="E"
dic[15]="F"

def change(num,n):
    if num==0:
        return "0"
    result=""
    while True:
        if num==0:
            break
        a=num%n
        if a>=10:
            result=dic[a]+result
        else:
            result=str(a)+result
        num=num//n
    return result


def solution(n, t, m, p):
    answer = ''
    s=""
    for i in range(p+(t-1)*m):
        s+=change(i,n)

    for i in range(t):
        answer=answer+s[p-1+i*m]
        
    return answer