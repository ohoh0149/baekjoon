import sys
input=sys.stdin.readline
s1=input()
s2=input()
s1=s1[:-1]
s2=s2[:-1]

l=len(s2)
lst=[]
lst_len=0
for s in s1:
    lst.append(s)
    lst_len+=1

    temp="".join(lst[-l:])
    if temp==s2:
        for _ in range(l):
            lst.pop()
        # lst=lst[:-l]
        # lst_len-=(l-1)

if not lst:
    print("FRULA")
else:
    print("".join(lst))




