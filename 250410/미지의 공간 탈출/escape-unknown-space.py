from collections import deque
n,m,F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr3 = [[list(map(int, input().split())) for _ in range(m)] for _ in range(5)]
wall = [list(map(int,input().split())) for _ in range(F)]

def find_3d_start():
    for i in range(m):
        for j in range(m):
            if arr3[4][i][j]== 2:
                return 4,i,j

def find_2d_end():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 4:
                arr[i][j]=0
                return i,j

def find_3d_base():
    for i in range(m):
        for j in range(m):
            if arr[i][j] == 3:
                return i,j
def find_out():
    bi,bj = find_3d_base()

    for i in range(bi,bi+m):
        for j in range(bj,bj+m):
            if arr[i][j] != 3:
                continue
            if arr[i][j+1] == 0: #우측출구
                return 0,m-1,(m-1)-(i-bi),i,j+1
            elif arr[i][j-1] == 0:
                return 1, m-1, i-bi, i,j-1
            elif arr[i+1][j] == 0:
                return 2, m-1, j-bj, i+1,j
            elif arr[i-1][j]==0:
                return 3, m-1, (m-1) - (j-bj), i-1,j 
left = {0:2, 1:3, 2:1, 3:0}
right = {0:3, 1:2, 2:0, 3:1}
def bfs_3d(sk,si,sj,oz,oi,oj):
    q = deque()
    visited = [[[0]*m for _ in range(m)]for _ in range(5)]

    q.append((sk,si,sj))
    visited[sk][si][sj] = 1

    while q:
        ck, ci, cj = q.popleft()

        if (ck,ci,cj) == (oz,oi,oj):
            return visited[ck][ci][cj]
        
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = di+ci, dj+cj
            if ni<0:
                if ck==0: nk,ni,nj = 4, (m-1)-cj, m-1
                elif ck==1: nk,ni,nj = 4, cj, 0
                elif ck==2: nk,ni,nj = 4, m-1, cj
                elif ck==3: nk,ni,nj = 4, 0, (m-1)-cj
                elif ck==4: nk,ni,nj = 3, 0, (m-1)-cj
            elif ni>=m:
                if ck == 4: nk,ni,nj = 2, 0, cj
                else: continue
            elif nj <0:
                if ck == 4: nk,ni,nj = 1, 0, ci
                else:
                    nk,ni,nj = left[ck], ci, m-1
            elif nj >=m:
                if ck==4: nk,ni,nj = 0, 0, (m-1)-ci
                else:
                    nk,ni,nj = right[ck], ci, 0
            else:
                nk = ck
            if visited[nk][ni][nj] == 0 and arr3[nk][ni][nj] == 0:
                q.append((nk,ni,nj))
                visited[nk][ni][nj] = visited[ck][ci][cj]+1
    return -1

def bfs_2d(v, dist, si, sj, ei, ej):
    q = deque()
    q.append((si,sj))
    v[si][sj] = dist

    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):
            return v[ci][cj]
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = di+ci, dj+cj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]==0 and v[ci][cj]+1<v[ni][nj]:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
    return -1
#1. 위치 찾기
sk, si_3d, sj_3d= find_3d_start()
ei, ej= find_2d_end()
oz, oi, oj, si, sj= find_out()

#3d에서 bfs돌기
dist = bfs_3d(sk,si_3d,sj_3d,oz,oi,oj)

di = [0,0,1,-1]
dj = [1,-1,0,0]
if dist!=-1:
    #확산이 몇초까지 가는지 보는 과정
    visit = [[401]*n for _ in range(n)]

    for wi, wj, wd, wv in wall:
        visit[wi][wj] = 1
        cur_i, cur_j = wi, wj
        for mul in range(1, n+1):
            cur_i += di[wd]
            cur_j += dj[wd]
            if 0 <= cur_i < n and 0 <= cur_j < n and arr[cur_i][cur_j] == 0 and (cur_i, cur_j) != (ei, ej):
                visit[cur_i][cur_j] = min(visit[cur_i][cur_j], wv * mul)
            else:
                break


    dist = bfs_2d(visit, dist, si, sj, ei, ej)

print(dist)