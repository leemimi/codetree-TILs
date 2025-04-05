from collections import deque
n = int(input())
tmp = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
arr =[[[] for _ in range(n)] for _ in range(n)]

for _ in range(n*n):
    target, l1,l2,l3,l4 =map(int, input().split())
    like = [l1,l2,l3,l4]
    candidate = []

    for i in range(n):
        for j in range(n):
            if tmp[i][j]!=0:
                continue
            likecnt = empcnt = 0
            for k in range(4):
                nx =i + dx[k]
                ny= j +dy[k]
                if 0<=nx<n and 0<=ny<n:
                    if tmp[nx][ny] in like:
                        likecnt+=1
                    if tmp[nx][ny] == 0:
                        empcnt +=1
                    candidate.append([likecnt,empcnt, i,j])
    candidate.sort(key = lambda x:(-x[0],-x[1],x[2],x[3]))

    r,c = candidate[0][2], candidate[0][3]
    tmp[r][c] = target
    arr[r][c] = like

answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx, ny = i+dx[k],j+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if tmp[nx][ny] in arr[i][j]:
                    cnt+=1
        if cnt!=0:
            answer += 10**(cnt-1)
print(answer)

