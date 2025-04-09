from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
store = {}
for k in range(1,m+1):
    i,j = map(int, input().split())
    store[k] = (i-1,j-1)

basecamp = set()
#0처리하고 베이스캠프 도착하면 다시 1처리하기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            basecamp.add((i,j))
            arr[i][j]=0

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def find(si,sj,dists):
    global arr
    q = deque()
    visited = [[0]*n for _ in range(n)]
    q.append((si,sj))
    wb = []
    visited[si][sj]=1
    while q:
        #동일 범위까지만!!
        nq = deque()
        for x,y in q:
            if (x,y) in dists:
                wb.append((x,y))
            else:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                        if arr[nx][ny] == 0:
                            nq.append((nx,ny))
                            visited[nx][ny]=1

        if len(wb)>=1:
            wb.sort()
            return wb[0]
        q= nq
    return -1




def simulate():
    time = 1
    q = deque()
    arrived = [0]*(m+1)

    #편의점 찾아가자
    while q or time==1:
        #같은 범위 내에서 편의점 찾기 위해 큐를 하나 더 만듬
        nq = deque()
        lst = []
        for ci,cj,member in q:
            if arrived[member] ==0:
                ai,aj = find(store[member][0],store[member][1],set(((ci+1,cj),(ci-1,cj),(ci,cj+1),(ci,cj-1))))
                if (ai,aj) == store[member]:
                    arrived[member]=time
                    lst.append((ai,aj))
                else:
                    nq.append((ai,aj,member))
        q = nq
        #편의점 도착 처리
        if len(lst)>0:
            for i,j in lst:
                arr[i][j] = 1

        #베이스 캠프 도착하기(시간에 맞는 사람이 이동함)
        if time<=m:
            si,sj = store[time]
            ei,ej = find(si,sj,basecamp)
            basecamp.remove((ei,ej))
            arr[ei][ej] = 1
            q.append((ei,ej,time))

        time+=1
    return max(arrived)

answer= simulate()
print(answer)