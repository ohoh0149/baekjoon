n=int(input())
count=0
lst=[]
def dfs(k,s):
    global count,lst
    count+=1
    if count>1000000:
        return

    for i in range(10):
        if s and int(s[-1])==i:
            break
        lst.append(int(s+str(i)))
        dfs(k+1,s+str(i))

dfs(0,"")
lst.sort()
if n<len(lst):
    print(lst[n])
else:
    print(-1)
#
# num=0
# count=-1
# result=-1
# def check(num):
#     s_num=str(num)
#     ans=True
#     for i in range(len(s_num)-1):
#         if s_num[i]<=s_num[i+1]:
#             ans=False
#             break
#     return ans
#
#
# while True:
#     if num>9876543210:
#         break
#     if count>1000000:
#         break
#     if check(num):
#         count+=1
#
#     if count==n:
#         result=num
#         break
#     num+=1
# print(result)
