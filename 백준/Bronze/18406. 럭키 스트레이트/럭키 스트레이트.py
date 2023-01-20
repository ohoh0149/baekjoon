import sys
sys.stdin.readline
str=input()

n=len(str)
a=sum(list(map(int,list(str[:n//2]))))
b=sum(map(int,list(str[n//2:])))
#print(a,b)

if a==b:
    print("LUCKY")
else:
    print("READY")