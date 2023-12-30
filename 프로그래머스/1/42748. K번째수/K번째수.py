def solution(array, commands):
    answer = []
    for i,j,k in commands:
        lst=array[i-1:j].copy()
        lst.sort()
        #print(lst)
        answer.append(lst[k-1])
    return answer