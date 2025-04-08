from collections import defaultdict,deque
n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]


def bfs(x,y,visited,color):
    q = deque()
    visited[x][y] = 1
    q.append((x,y))
    lst = []
    lst.append((x,y))
    while q:
        ci,cj = q.popleft()

        for i in range(4):
            nx = ci+dx[i]
            ny = cj+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if color == arr[nx][ny]:
                    visited[nx][ny] = 1
                    lst.append((nx,ny))
                    q.append((nx,ny))
    return lst

def get_sums(alst, blst):
    bset = set(blst)
    cnt = 0
    for a, b in alst:
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if (nx, ny) in bset:
                cnt += 1
    return cnt


def rotate(x,y,r):
    for i in range(r):
        for j in range(r):
             tmp[x+j][y+r-1-i] = arr[x+i][y+j]


answer = 0
for _ in range(4):
    

    #그룹 만들기
    visited = [[0]*n for _ in range(n)]
    dicts = defaultdict(list)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                group = bfs(i,j,visited,arr[i][j])
            
                dicts[cnt] = group
                cnt+=1

    #조화로움 계산
    max_total = 0
    N = len(dicts)
    for i in range(N):
        for j in range(i+1,N):
            total = 0
            #칸의수
            a = len(dicts[i])+len(dicts[j])
            #숫자값들
            b= arr[dicts[i][0][0]][dicts[i][0][1]]

            c= arr[dicts[j][0][0]][dicts[j][0][1]]
            
            d = get_sums(dicts[i],dicts[j])
            total = a*b*c*d
            if total < 1:
                continue
            else:
                answer += total

    #회전하기
    tmp = [[0]*n for _ in range(n)]
    mid = n//2
    #4개 시계
    rotate(0,0,mid)
    rotate(0,mid+1,mid)
    rotate(mid+1,0,mid)
    rotate(mid+1,mid+1,mid)

    #십자가 반시계
    mid = n // 2
    for i in range(n):
        # 중앙 열 → 중앙 행 (반시계 회전)
        tmp[mid][i] = arr[i][mid]
        # 중앙 행 → 중앙 열 (반시계 회전)
        tmp[n - 1 - i][mid] = arr[mid][i]

    arr = tmp


print(answer)