def in_range(x,y):
    return 0<=x<n and 0<=y<m

def print_arr(arr):
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end="")
        print()

def print_state():
    print("Passed Turns :",pass_turn)
    print("LV :",lv)
    print("HP :",str(hp)+"/"+str(max_hp))
    print("ATT :",str(attack)+"+"+str(w_attack))
    print("DEF :",str(defense)+"+"+str(a_defense))
    print("EXP :",str(exp)+"/"+str(max_exp))
    #print(o_set)



def get_item(x,y):
    global w_attack
    global a_defense
    global o_set
    global arr
    if item_arr[x][y][0]=="W":
        w_attack=item_arr[x][y][1]
    elif item_arr[x][y][0]=="A":
        a_defense=item_arr[x][y][1]
    elif item_arr[x][y][0]=="O":
        o_type=item_arr[x][y][1]
        if o_type in o_set or len(o_set)>=4:
            pass
        else:
            o_set.add(o_type)

    else:
        print("There is no item!! error!")

    item_arr[x][y]=0
    arr[x][y]="."
def get_exp(val):
    global exp,lv,max_exp
    global max_hp,attack,defense,hp
    if "EX" in o_set:
        exp+=int(val*1.2)
    else:
        exp+=val
    if exp>=max_exp:
        lv+=1
        max_hp+=5
        attack+=2
        defense+=2
        hp=max_hp
        max_exp=lv*5
        exp=0



def fight(x,y):
    global hp,arr,mx,my
    global name
    m_name,m_attack,m_defense,m_max_hp,m_exp=mon_arr[x][y]
    m_hp=m_max_hp
    total_attack=attack+w_attack
    total_defense=defense+a_defense
    count=0
    while True:
        if count==0 and "CO" in o_set:
            if "DX" in o_set:
                m_hp-=max(1,total_attack*3-m_defense)
            else:
                m_hp-=max(1,total_attack*2-m_defense)
        else:
            m_hp-=max(1,total_attack-m_defense)
        #몬스터 사망
        if m_hp<=0:
            #print("몬스터 사망")
            arr[x][y]="."
            get_exp(m_exp)
            if "HR" in o_set:
                hp+=3
                if hp>max_hp:
                    hp=max_hp
            break

        if count==0 and arr[x][y]=="M" and "HU" in o_set:
            pass
        else:
            hp-=max(1,m_attack-total_defense)
        #주인공 사망
        if hp<=0:
            #print("주인공 사망")
            name=m_name
            if "RE" in o_set:
             #   print("부활")
                o_set.remove("RE")
                hp = max_hp
                mx, my = sx, sy
            break
        count+=1






dx=[-1,0,1,0]
dy=[0,1,0,-1]
map_d=dict()
map_d["U"]=0
map_d["R"]=1
map_d["D"]=2
map_d["L"]=3

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    inp=input()
    lst=[]
    for s in inp:
        lst.append(s)
    arr.append(lst)

move_d=input()
#몬스터 수, 아이템 상자 수
num_mon,num_item=0,0
for i in range(n):
    for j in range(m):
        if arr[i][j] in ["&","M"]:
            num_mon+=1
        elif arr[i][j]=="B":
            num_item+=1
        elif arr[i][j]=="@":
            mx,my=i,j
            arr[i][j]="."
mon_arr=[[0]*m for _ in range(n)]
item_arr=[[0]*m for _ in range(n)]

for _ in range(num_mon):
    inp=input().split()
    r,c=int(inp[0])-1,int(inp[1])-1
    mon_arr[r][c]=[inp[2]]+list(map(int,inp[3:]))

for _ in range(num_item):
    inp = input().split()
    r, c = int(inp[0]) - 1, int(inp[1]) - 1
    if inp[2] in ["W","A"]:
        item_arr[r][c]=[inp[2],int(inp[3])]
    else:
        item_arr[r][c] = inp[2:]

hp=20
max_hp=20
attack=2
defense=2
lv=1
exp=0
max_exp=5*lv
w_attack=0
a_defense=0
o_set=set()
name=""

pass_turn=0
kill_boss=False
#현재 주인공 좌표 mx,my

sx,sy=mx,my
for idx,d in enumerate(move_d,start=1):
    #print(idx)
    d=map_d[d]
    nx=mx+dx[d]
    ny=my+dy[d]
    # 격자 밖이거나 벽이 있는 경우 제자리
    if not in_range(nx,ny) or arr[nx][ny]=="#":
        nx,ny=mx,my
    #print("-------------turn start-------------")
    #print("d:",d)
    #print(mx,my,"->",nx,ny)
    mx,my=nx,ny
    if arr[mx][my]==".":
        pass
    elif arr[mx][my]=="B":
        get_item(mx,my)
    elif arr[mx][my]=="^":
        if "DX" in o_set:
            hp-=1
        else:
            hp-=5
        if hp<=0 and "RE" in o_set:
            o_set.remove("RE")
            hp=max_hp
            mx,my=sx,sy
        if hp<=0:
            name="SPIKE TRAP"
    elif arr[mx][my]=="&":
        fight(mx,my)
    elif arr[mx][my]=="M":
        ax,ay=mx,my
        if "HU" in o_set:
            hp=max_hp
        fight(mx,my)
        if arr[ax][ay]==".":
            #print("보스 사망")
            kill_boss=True


    pass_turn=idx
    if hp<=0 or kill_boss:
        break

if hp<=0:
    hp=0
if hp>0:
    arr[mx][my]="@"
print_arr(arr)
print_state()

if kill_boss:
    print("YOU WIN!")
elif hp<=0:
    print("YOU HAVE BEEN KILLED BY",name+"..")
else:
    print("Press any key to continue.")











