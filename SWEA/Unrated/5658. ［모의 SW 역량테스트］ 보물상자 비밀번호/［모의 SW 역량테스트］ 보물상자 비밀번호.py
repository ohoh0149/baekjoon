


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
dic={}
dic["0"]=0
dic["1"]=1
dic["2"]=2
dic["3"]=3
dic["4"]=4
dic["5"]=5
dic["6"]=6
dic["7"]=7
dic["8"]=8
dic["9"]=9
dic["A"]=10
dic["B"]=11
dic["C"]=12
dic["D"]=13
dic["E"]=14
dic["F"]=15
def turn(s):
    new_s=s[-1]+s[:-1]
    return new_s
def make_ten(s):
    result=0
    for i in range(l-1,-1,-1):
        result+=dic[s[l-1-i]]*pow(16,i)
        #print(result)
    return result

def make_ten_lst(s):
    global lst
    for i in range(0,len(s),l):
        lst.append(make_ten(s[i:i+l]))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    lst=[]
    n,k=map(int,input().split())
    s=input()
    l=len(s)//4
    make_ten_lst(s)

    for i in range(l-1):
        s=turn(s)
        make_ten_lst(s)
    lst=list(set(lst))
    lst.sort(reverse=True)
    #print(lst)
    print("#"+str(test_case),lst[k-1])


    # ///////////////////////////////////////////////////////////////////////////////////
