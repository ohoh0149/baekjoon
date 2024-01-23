t=int(input())

for _ in range(t):
    st=input()

    count=0
    ans=""
    for s in st:
        if s=="(":
            count+=1
        else:
            if count==0:
                ans="NO"
                break
            count-=1

    if ans=="NO" or count!=0:
        print("NO")
        continue
    else:
        print("YES")



