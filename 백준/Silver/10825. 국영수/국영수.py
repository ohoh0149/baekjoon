n=int(input())
arr=[]
for i in range(n):
    a,b,c,d=input().split()
    b=int(b)
    c=int(c)
    d=int(d)
    arr.append((a,b,c,d))
#print(arr)
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[3],reverse=True)
arr.sort(key=lambda x:x[2])
arr.sort(key=lambda x:x[1],reverse=True)

for i in arr:
    print(i[0])