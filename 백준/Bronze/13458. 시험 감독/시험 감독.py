n=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())

result=0
for i,num in enumerate(A):
    result+=1
    if num>B:
        result+=(num-B)//C
        if (num-B)%C!=0:
            result+=1

print(result)
