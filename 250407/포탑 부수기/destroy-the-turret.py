from collections import deque
n,m,K= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
#공격한 애들(i,j)
potab = []
turn = [[0]*m for _ in range(n)]

def attack(si,sj,ei,ej,arr):
    q = deque()
    visited = [[[] for _ in range(m)] for _ in range(n)]
    q.append((si,sj))
    visited[si][sj] = (si,sj)
    damage = arr[si][sj]
    #우 하 좌 상
    while q:
        x,y = q.popleft()
        if (x,y) == (ei,ej):
            arr[ei][ej] = max(0, arr[ei][ej]-damage)
            while True:
                #직전좌표
                x,y = visited[x][y]
                if (x,y) == (si,sj):
                    return True
                arr[x][y] = max(0, arr[x][y]- damage//2)
                fight.add((x,y))
        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            nx = (di+x)%n
            ny = (dj+y)%m
            if len(visited[nx][ny])==0 and arr[nx][ny]>0:
                q.append((nx,ny))
                visited[nx][ny] = (x,y)
    return False
            
def bomb(si,sj,ei,ej):
    damage = arr[si][sj]
    
    arr[ei][ej] = max(0, arr[ei][ej]-damage)

    for di,dj in ((0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,-1),(-1,-1),(1,1)):
        nx = (di+ei)%n
        ny = (dj+ej)%m
        if (nx,ny) != (si,sj):
            arr[nx][ny] = max(0,arr[nx][ny]-damage//2)
            fight.add((nx,ny))    


                                   




for t in range(K):
    #공격자 선정
    max_val = 50001
    mx_turn = 0
    si = -1
    sj = -1
    for i in range(n):
        for j in range(m):
            if arr[i][j] <= 0:
                continue
            if max_val > arr[i][j] or (max_val==arr[i][j] and mx_turn<turn[i][j]) or \
             (max_val==arr[i][j] and mx_turn==turn[i][j] and si+sj < i+j) or \
             (max_val==arr[i][j] and mx_turn==turn[i][j] and si+sj == i+j and sj < j):
                max_val = arr[i][j]
                mx_turn = turn[i][j]
                si = i
                sj = j

    #공격자 선정
    mx = 0
    min_turn = K+1
    ei = n
    ej = m
    for i in range(n):
        for j in range(m):
            if arr[i][j] <= 0:
                continue
            if mx < arr[i][j] or (mx==arr[i][j] and min_turn > turn[i][j]) or \
            (mx ==arr[i][j] and min_turn == turn[i][j] and ei+ej > i+j) or \
            (mx ==arr[i][j] and min_turn == turn[i][j] and ei+ej == i+j and ej>j):
                mx = arr[i][j]
                min_turn = turn[i][j]
                ei = i
                ej = j
    
    #레이저 공격
    arr[si][sj] += m+n
    turn[si][sj] = t+1
    fight = set()
    fight.add((si,sj))
    fight.add((ei,ej))
    flag = attack(si,sj,ei,ej,arr)
    if not flag:
        bomb(si,sj,ei,ej)

    for i in range(n):
        for j in range(m):
            if arr[i][j] >0 and (i,j) not in fight:
                arr[i][j]+=1
    
    cnt = n*m
    for s in arr:
        cnt -= s.count(0)
    if cnt <=1:
        break

print(max(map(max, arr)))