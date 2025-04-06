from collections import deque
N,M,Q = map(int, input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dirs(x,y, d):
    if d == 0:
        return [x-1,y]
    elif d ==1 :
        return [x,y+1]
    elif d==2:
        return [x+1,y]
    else:
        return [x,y-1]

arr = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]
v = [[0]*(N+2) for _ in range(N+2)]

units = {}
hp_k = [0]*(M+1)
for i in range(1,M+1):
    r,c,h,w,k = map(int,input().split())
    units[i] = [r,c,h,w,k]
    hp_k[i] = k

def push_unit(start, dir):
    q = deque() #밀릴것들
    p_set = set() #이동되는 기사 번호
    damage = [0]*(M+1)
    
    q.append(start)
    pset.add(start)
    while q:
        x = q.popleft()
        ci,cj,h,w,k = units[x]

        #명령 받은 방향 이동되는지? 벽이 아니어야함. 벽이면 return, 겹치면 밀림 그럼 q넣기
        nx,ny = ci+dx[dir], cj+dy[dir]
        for i in range(nx, nx+h):
            for j in range(ny, ny+w):
                if arr[i][j] == 2:
                    return
                elif arr[i][j] == 1:
                    damage[x] +=1
        
        for ids in units:
            if ids in pset: continue
            ti,tj,th,tw,tk = units[ids]

            #겹치는 경우
            if nx<= ti+th-1 and nx+h-1 >= ti and ny<=tj+tw-1 and ny+w-1 >= tj:
                q.append(ids)
                p_set.add(ids)
 
    damage[start] = 0
    #이동, 데미지 체력 이상 이면 삭제처리
    for idx in p_set:
        si,sj,h,w,k = units[idx]

        if k<=damage[idx]:
            units.pop(idx)
        else:
            ni,nj = si+dx[dir], sj+dy[dir]
            units[idx] = [ni,nj,h,w,k-damage[idx]]



for _ in range(Q):
    idx,d = map(int, input().split())
    if idx in units:
        push_unit(idx, d)

answer= 0
for u in units:
    answer += hp_k[u]-units[u][4]
print(answer)