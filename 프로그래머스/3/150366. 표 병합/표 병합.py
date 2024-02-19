arr=[[0]*51 for _ in range(51)]

def solution(commands):
    global arr
    # for i in range(1,51):
    #     print(arr[i])
    answer = []
    set_lst=[]
    for command in commands:
        #print(set_lst)
        c=list(command.split())
        if c[0]=="UPDATE" and len(c)==4:

            r,c,val=int(c[1]),int(c[2]),c[3]

            s_idx=-1
            for idx,s in enumerate(set_lst):
                if (r,c) in s:
                    s_idx=idx
            if s_idx==-1:
                arr[r][c]=val
            else:

                for x,y in set_lst[s_idx]:
                    arr[x][y]=val
                    
                
        elif c[0]=="UPDATE" and len(c)==3:
            for i in range(1,51):
                for j in range(1,51):
                    if arr[i][j]==c[1]:
                        arr[i][j]=c[2]
                    
        elif c[0]=="MERGE":
            r1,c1,r2,c2=map(int,c[1:])
            #같은 위치일 경우 무시
            if (r1,c1)==(r2,c2):
                continue
                
            if arr[r1][c1]!=0:
                val=arr[r1][c1]
            else:
                val=arr[r2][c2]
            pos1_idx=-1
            pos2_idx=-1
            for idx,s in enumerate(set_lst):
                if (r1,c1) in s:
                    pos1_idx=idx
                if (r2,c2) in s:
                    pos2_idx=idx
            #둘이 이미 병합되어 있음
            if pos1_idx!=-1 and pos1_idx==pos2_idx:
                continue
            #둘다 홀로 존재
            if pos1_idx==-1 and pos2_idx==-1:
                set_lst.append(set([(r1,c1),(r2,c2)]))
                arr[r1][c1]=val
                arr[r2][c2]=val
                continue
            #pos1만 홀로존재
            if pos1_idx==-1 and pos2_idx!=-1:
                set_lst[pos2_idx].add((r1,c1))
                temp_s=set_lst[pos2_idx]
                for x,y in temp_s:
                    arr[x][y]=val
                continue
            #pos2만 홀로존재
            if pos2_idx==-1 and pos1_idx!=-1:
                set_lst[pos1_idx].add((r2,c2))
                temp_s=set_lst[pos1_idx]
                for x,y in temp_s:
                    arr[x][y]=val
                continue
            #둘다 각각의 집합에 존재
            s1=set_lst[pos1_idx]
            s2=set_lst[pos2_idx]
            new_set=s1.union(s2)
        
            for x,y in new_set:
                arr[x][y]=val
            set_lst.remove(s1)
            set_lst.remove(s2)
            set_lst.append(new_set)
            

            
            
            
        elif c[0]=="UNMERGE":
            r,c=map(int,c[1:])
            s_idx=-1
            for idx,s in enumerate(set_lst):
                if (r,c) in s:
                    s_idx=idx
            if s_idx!=-1:
                val=arr[r][c]
                temp_s=set_lst[s_idx]
                del set_lst[s_idx]
                
                for x,y in temp_s:
                    arr[x][y]=0
                arr[r][c]=val
                
                
                
                
                    
                
        else:
            #r,c=map(int,c[1:])
            r,c=int(c[1]),int(c[2])
            if arr[r][c]==0:
                answer.append("EMPTY")
            else:
                answer.append(arr[r][c])
        
        
        
    return answer