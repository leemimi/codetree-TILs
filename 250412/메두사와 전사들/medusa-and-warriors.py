n,m = map(int, input().split())
si,sj,ei,ej = map(int,input().split())
p = list(map(int, input().split()))
people = []
for i,j in range(0,m*2,2):
    people.append((p[i],p[i+1]))

arr = [list(map(int, input().split()))for _ in range(n)]

def find_route(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    visited = [[0]*n for _ in range(n)]
    visited[si][sj] = ((si,sj))

    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):
            route = []
            ci,cj = visited[ci][cj]
            while (ci,cj) != (si,sj):
                route.append((ci,cj))
                ci,cj = visited[ci][cj]
            return route[::-1]
        
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = di+ci, dj+cj
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==0 and arr[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = (ci,cj)
    return -1

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def make_safe(v, si, sj, dr, org_dr):
    ci,cj = si+di[dr], sj+dj[dr]
    make_line(visited,ci,cj,dr)
    ci,cj = si+di[org], sj+dj[org]
    while 0<=ci<N and 0<=cj<N:          # 범위내라면 계속 진행
        mark_line(v, ci, cj, dr)        # v에 dr방향으로 이동가능지역 표시
        ci,cj = ci+di[org_dr],cj+dj[org_dr]

def make_line(visited, ci,cj,dr):
    while 0<=ni<N and 0<=nj<N:
        visited[ci][cj] = 2
        ci,cj = ci+di[dr], cj+dj[dr]

def make_stone(marr,mi,mj,dr):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    ni = di[dr]+mi
    nj = dj[dr]+mj
    while 0<=ni<n and 0<=nj<n:
        visited[ni][nj]=1
        if marr[ni][nj]>0:
            cnt+=marr[ni][nj]
            ni,nj = ni+di[dr],nj+dj[dr]
            make_line(visited,ni,nj,dr)
            break
        ni,nj = ni+di[dr],nj+dj[dr]
    
    for org in ((dr-1)%8, (dr+1)%8):
        si,sj = mi + di[org], mj + dj[org]
        while 0<=si<N and 0<=sj<N:
            if visited[si][sj] == 0 and marr[si][sj] > 0:
                visited[si][sj] = 1
                cnt += marr[si][sj]
                make_safe(visited, si,sj,dr,org)
                break
            ci,cj = si,sj
            while 0<=ci<N and 0<=cj<N:
                if visited[ci][cj] == 0:
                    visited[ci][cj] = 1
                    if marr[ci][cj] > 0:
                        cnt += marr[ci][cj]
                        make_safe(visited,ci,cj,dr,org)
                        break
                else:
                    break
                ci,cj = ci+di[dr], cj+dj[dr]
            si,sj = si+di[org], sj+dj[org]
    return visited, cnt



#공원으로 갈 수 있는 경로 담은 배열
route = find_route(si,sj,ei,ej)

if route == -1:
    print(-1)
else:
    #경로에서 출발하기
    for mi,mj in route:
        move_cnt, attack_cnt = 0,0
        for i in range(len(people)-1,-1,-1):
            if people[i] == [mi,mj]:
                people.pop(i)
                
        #메두사 시선 시작
        #1.상하좌우 4방향으로 메두사 시선 들어오는 병정 얼마인지 갯수 세기
        marr = [[0]*n for _ in range(n)]
        for ti,tj in people:
            marr[ti][tj] +=1
        mx_stone = -1
        v = []
        for dr in range(0,4,6,2):
            tv, tstone = make_stone(marr,mi,mj,dr)
            if mx_stone < tstone:
                mx_stone = tstone
                v = tv
        
        move_cnt, attack_cnt = move_men(v, mi,mj)


