from collections import deque
n,m = map(int, input().split()) #m - 빨 제외 수갯수
arr = [list(map(int, input().split()))for _ in range(n)]
answer = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]
empty = (-1, -1, -1, -1)

tmp = [[-2 for _ in range(n)]for _ in range(n)]

def find_bomb_mix(a,b):
    q = deque()
    visited = [[False]*n for _ in range(n)]
    visited[a][b] = True
    q.append((a,b))
    color = arr[a][b]
    while q:
        x, y= q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and  0<=ny<n and not visited[nx][ny]:
                if arr[nx][ny] == 0 or arr[nx][ny] == color:
                    q.append((nx,ny))
                    visited[nx][ny] = True

    color_cnt, red = 0,0
    standard = (-1,-1)
    #폭탄 묶음 크기, 빨간색 수, 행, 열
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                continue
            color_cnt+=1

            if arr[i][j]==0:
                red+=1
            elif (i,-j) > standard:
                standard = (i,-j)

    return (color_cnt, -red, standard[0], standard[1])

def bfs(x,y,c):
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((x,y))

    while q:
        xx,yy = q.popleft()
        for i in range(4):
            nx = xx+dx[i]
            ny = yy + dy[i]
            if 0<=nx<n and  0<=ny<n and not visited[nx][ny]:
                if arr[nx][ny] == 0 or arr[nx][ny] == c:
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return visited

def find_bomb():
    best = empty
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 1:
                bomb = find_bomb_mix(i,j)
                if best < bomb:
                    best= bomb
    return best 





def gravity():
    #임시 배열 초기화
    for i in range(n):
        for j in range(n):
            tmp[i][j] = -2
    
    for j in range(n):
        bottom = n-1
        for i in range(n-1,-1,-1):
            if arr[i][j] == -2:
                continue
            if arr[i][j] == -1:
                bottom = i
            tmp[bottom][j] = arr[i][j]
            bottom -=1
    for i in range(n):
        for j in range(n):
            arr[i][j] = tmp[i][j]

def rotate():
    #임시 배열 초기화
    for i in range(n):
        for j in range(n):
            tmp[i][j] = -2

    for j in range(n-1,-1,-1):
        for i in range(n):
            tmp[n-1-j][i] = arr[i][j]

    for i in range(n):
        for j in range(n):
            arr[i][j] = tmp[i][j]

def clean(x,y):
    v=bfs(x,y,arr[x][y])
    remove(v)
    gravity()

def remove(visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                arr[i][j] = -2

def simulate():
    global answer
    best_bomb = find_bomb()

    bomb_cnt, red_cnt, x,y = best_bomb

    if best_bomb == empty or bomb_cnt <=1:
        return False
    
    answer+= bomb_cnt*bomb_cnt
    clean(x,-y)
    rotate()
    gravity()

    return True


while True:
    #터질 폭탄 없을때  break
    go = simulate()
    if not go:
        break 
    


print(answer)