from collections import deque
N, M, P, C, D = map(int, input().split())
v = [[0]*N for _ in range(N)]

#루돌프 위치
ri, rj = map(lambda x:int(x)-1, input().split())
v[ri][rj]=-1
score = [0]*(P+1)
alive = [1]*(P+1)
alive[0] = 0                                # 첫 번째는 없는 산타
wakeup_turn = [1]*(P+1)
santa = [[N]*2 for _ in range(P+1)]
for _ in range(1, P + 1):
    n,i,j = map(int, input().split())
    santa[n]=[i-1,j-1]                      # i, j
    v[i-1][j-1] = n

def my_print(v):
    for i in range(N):
        print(*v[i])

def move_santa(cur, si,sj,di,dj,mul):
    q = [(cur, si,sj,mul)]
    while q:
        cur,ci,cj,mul = q.pop(0)

        ni,nj = ci+di*mul, cj+dj*mul
        if 0<=ni<N and 0<=nj<N:
            if v[ni][nj] == 0:
                v[ni][nj] = cur
                santa[cur] = [ni,nj]
                return
            else:
                q.append((v[ni][nj],ni,nj,1))
                v[ni][nj] =cur
                santa[cur] = [ni,nj]
        else:
            alive[cur] =0
            return



for turn in range(1,M+1):
    #모두 탈락이면 종료
    if alive.count(1) == 0:
        break
    
    mn = 2*N*2
    #[1] 루돌프 이동
    #산타에서 가까운 거리 찾기
    for idx in range(1,P+1):
        if alive[idx] == 0:
            continue
        
        si,sj = santa[idx]
        dist = (ri-si)**2+(rj-sj)**2
        if mn>dist:
            mn = dist
            mlst = [(si,sj,idx)]
        elif mn == dist:
            mlst.append((si,sj,idx))
    mlst.sort(reverse = True)
    si,sj,mn_idx= mlst[0]


    #[1-2]루돌프가 산타로 이동함
    rdi= rdj = 0
    if ri>si : rdi = -1
    elif ri<si : rdi = 1
    if rj > sj : rdj =-1
    elif rj<sj : rdj = 1

    v[ri][rj] = 0
    ri,rj = ri+rdi, rj+rdj
    v[ri][rj] = -1
    
    #산타랑 충돌했다면?
    if (ri,rj) == (si,sj):
        score[mn_idx] +=C
        wakeup_turn[mn_idx] = turn+2
        move_santa(mn_idx, si,sj,rdi,rdj,C)

    #[2] 산타의 움직임
    for idx in range(1,P+1):
        if alive[idx]==0:
            continue
        if wakeup_turn[idx]>turn:
            continue
        si,sj = santa[idx]
        mn_dist = (ri-si)**2+(rj-sj)**2
        tlst = []
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = di+si,  dj+sj
            dist = (ri-ni)**2 + (rj-nj)**2
            if 0<=ni<N and 0<=nj<N and v[ni][nj] <= 0:
                if mn_dist > dist:
                    mn_dist = dist
                    tlst.append((ni,nj,di,dj))
        
        if len(tlst) == 0:
            continue
        ni,nj,di,dj = tlst[-1]

        #루돌프와 충돌?
        if (ri,rj) == (ni,nj):
            score[idx] += D
            wakeup_turn[idx] = turn+2
            v[si][sj] = 0
            move_santa(idx, ni,nj,-di,-dj,D)
        else:
            v[si][sj] = 0
            v[ni][nj] = idx
            santa[idx] = [ni,nj]
    
    for i in range(1,P+1):
        if alive[i] == 1:
            score[i]+=1

print(*score[1:])
