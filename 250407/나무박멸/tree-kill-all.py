from collections import deque, defaultdict
n,m,K,c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
#빈칸0, 벽-1
answer = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

ddx = [-1, 1, 1, -1]
ddy = [-1, -1, 1, 1]

tree = [[0]*n for _ in range(n)]
tmp = [[0]*n for _ in range(n)]

def tree_grow():
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 1:
                cnt = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny] > 0:
                            cnt+=1
                arr[i][j] +=cnt

def tree_spread():
    for i in range(n):
        for j in range(n): 
            tmp[i][j] = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                cnt = 0
                q = deque()
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny] == 0 and tree[nx][ny] <=0:
                            cnt+=1
                            q.append((nx,ny))
                if cnt == 0:
                    continue
                while q:
                    x,y = q.popleft()
                    tmp[x][y] += arr[i][j]//cnt
    for i in range(n):
        for j in range(n):
            if tmp[i][j]>0:
                arr[i][j] += tmp[i][j]

def tree_remove():
    global answer
    dxs, dys = [-1, 1, 1, -1], [-1, -1, 1, 1]

    max_del = 0
    max_x = 0
    max_y = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] <=0:
                continue
            cnt = arr[i][j]
            for d in range(4):
                nx = i
                ny = j
                for _ in range(K):
                    nx = nx+dxs[d]
                    ny = ny+ dys[d]

                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny] <= 0:
                            break
                        cnt+=arr[nx][ny]

            if max_del < cnt:
                max_del = cnt
                max_x = i
                max_y = j
    answer += max_del

    if arr[max_x][max_y] > 0:
        arr[max_x][max_y] = 0
        tree[max_x][max_y] = c

        for dx, dy in zip(dxs, dys):
            nx, ny = max_x, max_y
            for _ in range(K):
                nx, ny = nx + dx, ny + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    break
                if arr[nx][ny] < 0:
                    break
                if arr[nx][ny] == 0:
                    tree[nx][ny] = c
                    break
                tree[nx][ny] = c
                arr[nx][ny] = 0

                        
def tree_age_del():
    for i in range(n):
        for j in range(n):
            if tree[i][j] > 0:
                tree[i][j] -=1



for _ in range(m):
    #나무 성장
    tree_grow()
    #나무 번식
    tree_spread()

    #제초지역 나이 감소
    tree_age_del()

    #제초제 뿌리기
    tree_remove()
print(answer)
