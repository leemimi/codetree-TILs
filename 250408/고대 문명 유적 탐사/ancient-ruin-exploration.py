from collections import deque
K,M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(5)]
nums = list(map(int, input().split())) #유물조각 번호
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def turns(narr, ci,cj):
    tmp = [x[:]for x in narr]
    for i in range(3):
        for j in range(3):
            tmp[i+ci][cj+j] = arr[ci+3-j-1][cj+i]
    return tmp

def bfs(arr,visited,x,y,flag):
    q = deque()
    visited[x][y] = 1
    #유물의 수
    cnt = 0
    vset = set()

    vset.add((x,y))
    q.append((x,y))
    cnt+=1

    while q:
        xx,yy= q.popleft()
        for k in range(4):
            nx = xx+dx[k]
            ny = yy+dy[k]
            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0 and arr[nx][ny] == arr[xx][yy]:
                q.append((nx,ny))
                visited[nx][ny]=1
                vset.add((nx,ny))
                cnt+=1
    if cnt>=3:
        if flag == 1:
            for i,j in vset:
                arr[i][j] = 0
        return cnt
    else:
        return 0

def count_value(arr, flag):
    visited = [[0]*5 for _ in range(5)]
    cnt = 0

    for i in range(5):
        for j in range(5):
            if visited[i][j] == 0:
                f = bfs(arr,visited,i,j,flag)
                cnt+=f

    return cnt



answer = []
for turn in range(1,K+1):
    
    max_cnt = 0
    for t in range(1,4):
        for i in range(3):
            for j in range(3):
                tmp = [x[:]for x in arr]
                #회전 하기 90,,,
                for _ in range(t):
                    tmp = turns(tmp, i,j)
                
                #flag를 둬서 찾기 0, 1일땐 지우기
                c = count_value(tmp,0)
                if max_cnt<c:
                    max_cnt = c
                    marr = tmp
    if max_cnt ==0:
        break
    cnt = 0
    arr = marr
    #연쇄획득하기
    while True:
        zero = count_value(arr,1)
        if zero == 0:
            break
        cnt+=zero

        for j in range(5):
            for i in range(4,-1,-1):
                if arr[i][j] == 0:
                    arr[i][j]=nums.pop(0)
    
    answer.append(cnt)
print(*answer)

