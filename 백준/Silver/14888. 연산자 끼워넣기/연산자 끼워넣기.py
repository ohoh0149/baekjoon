import sys
input=sys.stdin.readline
n=int(input())

an=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
max_result=-1e9
min_result=1e9

def cal(count,result,add,sub,mul,div):
    # #print("count=",count)
    # print("result=",result)
    # print("asmd=",add,sub,mul,div)
    global max_result,min_result
    global an
    if count==n-1:
        if result>max_result:
            max_result=result
        if result<min_result:
            min_result=result
    else:
        if add>0:
            count+=1
            temp_result=result+an[count]
            add-=1
            cal(count,temp_result,add,sub,mul,div)
            count-=1
            add+=1
        if sub>0:
            count+=1
            temp_result=result-an[count]
            sub-=1
            cal(count,temp_result,add,sub,mul,div)
            count-=1
            sub+=1
        if mul>0:
            count+=1
            temp_result=result*an[count]
            mul-=1
            cal(count,temp_result,add,sub,mul,div)
            count-=1
            mul+=1
        if div>0:
            count+=1
            if result<0:
                temp_result=-result
                temp_result=temp_result//an[count]
                temp_result=-temp_result
            else:
                temp_result=result//an[count]
            div-=1
            cal(count,temp_result,add,sub,mul,div)
            count-=1
            div+=1

cal(0,an[0],add,sub,mul,div)
print(max_result)
print(min_result)