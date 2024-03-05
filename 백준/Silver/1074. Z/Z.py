n,r,c=map(int,input().split())


# result=0
# def fun(x,y,k):
#     global result
#     if k==1:
#         for i in range(2):
#             for j in range(2):
#                 if x+i==r and j+y==c:
#                     print(result)
#                     exit()
#                 result+=1
#         return
#
#     for i in range(2):
#         for j in range(2):
#             fun(x+(2**(k-1))*i,y+(2**(k-1))*j,k-1)
#
# fun(0,0,n)

result=0
def fun(x,y,k):
    if k==0:
        return
    global result
    l=2**(k-1)
    temp=4**(k-1)
    if x<l and y<l:
        pass
    elif x<l and y>=l:
        result+=temp
        y-=l
    elif x>=l and y<l:
        result+=2*temp
        x-=l
    else:
        result+=3*temp
        x-=l
        y-=l
    fun(x,y,k-1)


fun(r,c,n)
print(result)