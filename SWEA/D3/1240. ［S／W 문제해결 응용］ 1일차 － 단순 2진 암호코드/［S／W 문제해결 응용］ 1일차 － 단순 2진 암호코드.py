
#import sys
#sys.stdin = open("input.txt", "r")


def find_pos(arr):
    for i in range(n):
        for j in range(m-1,-1,-1):
            if arr[i][j]=="1":
                return i,j
    return -1,-1
def find_string(arr):
    x,y=find_pos(arr)

    return arr[x][y-55:y+1]

dic=dict()
dic["0001101"]=0
dic["0011001"]=1
dic["0010011"]=2
dic["0111101"]=3
dic["0100011"]=4
dic["0110001"]=5
dic["0101111"]=6
dic["0111011"]=7
dic["0110111"]=8
dic["0001011"]=9

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,m=map(int,input().split())
    arr=[]
    for _ in range(n):
        arr.append(input())

    s=find_string(arr)
    lst=[]
    for i in range(0,56,7):
        lst.append(int(dic[s[i:i+7]]))
    odd_sm=0
    for i in range(0,8,2):
        odd_sm+=lst[i]
    even_sm=sum(lst)-odd_sm
    result=0
    if (odd_sm*3+even_sm)%10==0:
        result=even_sm+odd_sm
    else:
        result=0

    print("#"+str(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
