n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
#print(arr)
sum=0
for i in range(n-1):
    arr[i+1]=arr[i]+arr[i+1]
    sum+=arr[i+1]
    if (i+3<n) and arr[i+1]<=arr[i+3]:
        continue
    for j in range(i+1,n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
        else:
            break

print(sum)