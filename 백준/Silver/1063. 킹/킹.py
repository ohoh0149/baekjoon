k_pos,r_pos,n=input().split()
n=int(n)
ky,kx=ord(k_pos[0])-65,8-int(k_pos[1])
ry,rx=ord(r_pos[0])-65,8-int(r_pos[1])
dic=dict()
dic["R"]=(0,1)
dic["L"]=(0,-1)
dic["B"]=(1,0)
dic["T"]=(-1,0)
dic["RT"]=(-1,1)
dic["LT"]=(-1,-1)
dic["RB"]=(1,1)
dic["LB"]=(1,-1)
def in_range(x,y):
    return 0<=x<8 and 0<=y<8
for _ in range(n):
    move=input()
    dx,dy=dic[move]

    nkx,nky=kx+dx,ky+dy
    if not in_range(nkx,nky):
        continue
    if nkx==rx and nky==ry:
        nrx,nry=rx+dx,ry+dy
        if not in_range(nrx,nry):
            continue
        kx,ky=nkx,nky
        rx,ry=nrx,nry
    else:
        kx,ky=nkx,nky


#print(kx,ky)
print(chr(ky+65)+str(8-kx))
#print(rx,ry)
print(chr(ry+65)+str(8-rx))

