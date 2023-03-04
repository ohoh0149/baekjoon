from itertools import combinations

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    n=int(input())
    s=[]
    for i in range(n):
        s.append(list(map(int,input().split())))

    comb_list=list(combinations(range(n),n//2))
    result=1e9
    for comb in comb_list:
        a=list(comb)
        b=[]
        a_flavor=0
        b_flavor=0
        for i in range(n):
            if i not in comb:
                b.append(i)
        a_list=list(combinations(a,2))
        b_list=list(combinations(b,2))
        for x,y in a_list:
            a_flavor+=s[x][y]
            a_flavor+=s[y][x]
        for x,y in b_list:
            b_flavor+=s[x][y]
            b_flavor+=s[y][x]
        result=min(result,abs(a_flavor-b_flavor))
    print("#"+str(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////
