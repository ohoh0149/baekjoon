def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    print(routes)
    p=0
    l=len(routes)
    while p<l:

        
        answer+=1
        
        val=routes[p][1]


                

        flag=False
        for i in range(p+1,l):
            if routes[i][0]<=val:
                continue
            else:
                flag=True
                p=i
                break
        if not flag:
            break
        
        

    return answer

# [-20                   -10]
#    [-18          -13]
#       [-17    -14]
#              [-14     -10]
#              [-14            -5]

#0           10
# 1          10
#  2 3
#      4 5


#              [-14                      -1]
#                             [-5  -3]
#                                           [0  3]