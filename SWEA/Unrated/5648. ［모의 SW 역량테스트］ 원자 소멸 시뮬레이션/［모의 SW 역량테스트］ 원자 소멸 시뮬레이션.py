
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    atom_list=[]
    n=int(input())
    for i in range(n):
        x,y,d,k=map(int,input().split())
        atom_list.append([2*x,2*y,d,k])
    result=0
    for _ in range(4000):
        
        for i in range(len(atom_list)):
            atom_list[i][0]+=dx[atom_list[i][2]]
            atom_list[i][1]+=dy[atom_list[i][2]]
        t=0
        index=0
        l=len(atom_list)
        while t<l:
            if atom_list[index][0]>2000 or atom_list[index][0]<-2000 or atom_list[index][1]>2000 or atom_list[index][1]<-2000:
                del atom_list[index]
                t+=1
            else:
                index+=1
                t+=1
                
            
        if len(atom_list)==1:
            break
        atom_list.sort(key=lambda x: (x[0],x[1]))
        remove_index_list=[]
        for i in range(len(atom_list)):
            if i==0 :
                if atom_list[i+1][0]==atom_list[i][0] and atom_list[i+1][1]==atom_list[i][1]:
                    remove_index_list.append(i)
            elif i==len(atom_list)-1:
                if atom_list[i][0]==atom_list[i-1][0] and atom_list[i][1]== atom_list[i-1][1]:
                    remove_index_list.append(i)
            else:
                if (atom_list[i + 1][0] == atom_list[i][0] and atom_list[i + 1][1] == atom_list[i][1]) or (atom_list[i][0]==atom_list[i-1][0] and atom_list[i][1]== atom_list[i-1][1]):
                    remove_index_list.append(i)
        remove_index_list.sort(reverse=True)
        for i in remove_index_list:
            result+=atom_list[i][3]
            del atom_list[i]



    print("#"+str(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////