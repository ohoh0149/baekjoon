n=int(input())
a_lst=list(map(int,input().split()))
b_lst=list(map(int,input().split()))
a_lst.sort()
b_lst.sort(reverse=True)
s=0
for a,b in zip(a_lst,b_lst):
    s+=a*b
print(s)

