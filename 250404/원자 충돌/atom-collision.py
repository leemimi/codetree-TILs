from collections import deque
n,m,k = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
info = []
for _ in range(m):
    x, y, m_, s, d = map(int, input().split())
    info.append([x-1, y-1, m_, s, d])  # ★ x-1, y-1 처리

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
info = deque(info)

def resplit(arr, dq):
    while dq:
        x,y,m,s,d = dq.popleft()
        arr[x][y].append((m,s,d))


def rerange(arr, dq):
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) > 1:
                total_m = 0
                total_s = 0
                dirs = []
                for m, s, d in arr[i][j]:
                    total_m += m
                    total_s += s
                    dirs.append(d)

                new_m = total_m // 5
                if new_m == 0:
                    arr[i][j] = []
                    continue
                new_s = total_s//len(arr[i][j])

                is_even = all(d%2==0 for d in dirs)
                is_odd = all(d%2!=0 for d in dirs)

                new_dirs = [0,2,4,6] if is_even or is_odd else [1,3,5,7]

                arr[i][j] = []
                for nd in new_dirs:
                    dq.append((i,j,new_m,new_s,nd))
            elif len(arr[i][j])==1:
                m, s, d = arr[i][j][0]
                dq.append((i, j, m, s, d))
                arr[i][j] = []

    resplit(arr, dq)




def go(arr, q):
    while q:
        x,y,m,s,d = q.popleft()
    
        nx = (x+dx[d]*s)%n
        ny = (y+dy[d]*s)%n

        arr[nx][ny].append((m,s,d))

    dq = deque()
    rerange(arr,dq)
    q.clear()
    for i in range(n):
        for j in range(n):
            for m,s,d in arr[i][j]:
                q.append((i,j,m,s,d))
            arr[i][j] = []

for _ in range(k):
    go(arr,info)

answer = 0

for x, y, m, s, d in info:
    answer += m

print(answer)
