n,w,l=map(int,input().split())
lst=list(map(int,input().split()))
q=[]

cur_idx=0
turn=0
left=l
length=0
while True:
    #q++
    if cur_idx==n and len(q)==0:
        break
    new_q=[]
    for truck in q:
        truck[1]+=1
        if truck[1]==w:
            length-=1
            left+=truck[0]
        else:
            new_q.append(truck)
    q=new_q
    if cur_idx<n and  lst[cur_idx]<=left and length<w:
        left-=lst[cur_idx]
        length+=1
        q.append([lst[cur_idx],0])
        cur_idx+=1
    turn+=1

print(turn)