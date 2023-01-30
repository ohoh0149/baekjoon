from bisect import bisect_left,bisect_right
def make_z(str):
    z_query=""
    for i in str:
        if i=="?":
            z_query+="z"
        else:       
            z_query+=i
    return z_query

def solution(words, queries):
    answer = []
    word_arr=[[] for i in range( 10001)] 
    for i in words:
        word_arr[len(i)].append(i)
    word_arr_reversed=[[] for i in range(10001)]
    for i in word_arr:
        for j in i:
            word_arr_reversed[len(j)].append(j[-1::-1])
    for i in word_arr:
        i.sort()
    for i in word_arr_reversed:
        i.sort()
        
    for query in queries:
        if query[0]!="?":#fro??
            length_query=len(query)
            z_query=make_z(query)
            left=bisect_left(word_arr[length_query],query)
            right=bisect_right(word_arr[length_query],z_query)
            # print(left,right)
            #print(right-left)
            answer.append(right-left)
        else:#???fro
            length_query=len(query)
            temp_query=query[-1::-1]
            z_query=make_z(temp_query)
            left=bisect_left(word_arr_reversed[length_query],temp_query)
            right=bisect_right(word_arr_reversed[length_query],z_query)
            # print(left,right)
            #print(right-left)
            answer.append(right-left)
    
    return answer