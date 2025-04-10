from collections import deque
n,m,k = map(int, input().split())
#0빈칸, 1머리사람, 2나머지, 3꼬리사람, 4이동 선
arr = [list(map(int, input().split()))for _ in range(n)]
dx = [0,-1, 0, 1]
dy = [1, 0,-1, 0]

def bfs(x,y,idx):
    q = deque()
    team = deque()
    team.append((x,y))
    q.append((x,y))
    visited[x][y] = 1
    arr[x][y] = idx
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = di+ci, cj+dj
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==0:
                if arr[ni][nj]==2:
                    q.append((ni,nj))
                    visited[ni][nj] = 1
                    team.append((ni,nj))
                    arr[ni][nj]=idx
                elif arr[ni][nj]==3:
                    ei,ej = ni, nj
                    visited[ni][nj]=1
    team.append((ei,ej))
    arr[ei][ej]=idx
    teams[idx]=team

visited = [[0]*n for _ in range(n)]
teams = {}
tm = 5
q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] ==1 and visited[i][j]==0:
            bfs(i,j,tm)
            tm+=1
answer = 0
for t in range(k):
    #1. 팀별로 1칸 이동
    for team in teams.values():
        ei,ej = team.pop()
        arr[ei][ej] = 4
        si,sj = team[0]

        for ni,nj in ((si-1,sj),(si+1,sj),(si,sj-1),(si,sj+1)):
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]==4:
                team.appendleft((ni,nj))
                arr[ni][nj] = arr[si][sj]
                break

    #2. 공발사하기
    dir = (t//n)%4 #방향 계산
    offset = t%n
    if dir == 0:
        ci,cj = offset, 0
    elif dir == 1:
        ci,cj = n-1,offset
    elif dir == 2:
        ci,cj = n-1-offset, n-1
    else:
        ci,cj = 0, n-1-offset
    
    for _ in range(n):
        if 0<=ci<n and 0<=cj<n and arr[ci][cj]>4:
            team_n = arr[ci][cj]
            answer += (teams[team_n].index((ci,cj))+1)**2
            teams[team_n].reverse()
            break
        ci,cj = ci+dx[dir], cj+dy[dir]
            
print(answer)