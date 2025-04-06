from collections import deque
R,C,K = map(int, input().split())
#출구정보
def getExit(x,y,d):
    if d==0:
        return [x-1,y]
    elif d==1:
        return [x,y+1]
    elif d==2:
        return [x+1,y]
    else:
        return [x,y-1]

answer = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
arr = [[0]*C for _ in range(R)]

def inBoard(nx,ny):
    if 0<=nx<R and 0<=ny<C:
        return True
    return False

def check(nx,ny):
    if 0<=nx<R and 0<=ny<C:
        if arr[nx][ny] == 0:
            return True
    else:
        if nx<R and 0<=ny<C:
            return True
    return False


#id는 정령 번호
def move(c,d,id):
    global arr
    x = -2
    y = c
    while True:
        if check(x+2,y) and check(x+1,y-1) and check(x+1,y+1):
            x+=1
        #서쪽 회전 이동
        elif check(x+1,y-1) and check(x-1,y-1) and check(x,y-2) and check(x+1,y-2) and check(x+2, y-1):
            x+=1
            y-=1
            d=(d-1)%4
        #동쪽 회전 후 이동
        elif check(x+1,y+1) and check(x-1,y+1) and check(x,y+2) and check(x+1,y+2) and check(x+2, y+1):
            x+=1
            y+=1
            d=(d+1)%4
        else:
            break

    if not inBoard(x,y) or not inBoard(x+1,y) or not inBoard(x,y-1) or not inBoard(x-1,y) or not inBoard(x,y+1):
        return [False,-1,-1]
    else:
        arr[x][y] = arr[x+1][y] = arr[x][y+1] = arr[x-1][y] = arr[x][y-1] = id
        gx,gy = getExit(x,y,d)
        arr[gx][gy] = -id
        return [True, x,y]    

def bfs(x,y,id):

    q = deque()
    q.append((x,y))
    vistied = [[False]*C for _ in range(R)]
    vistied[x][y] = True
    cand = []
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if not inBoard(nx,ny) or vistied[nx][ny] or arr[nx][ny]==0:
                continue
            # 절댓값이 같은 칸으로 움직이거나, 출구 칸에서 다른 칸으로 이동 가능
            if abs(arr[x][y])==abs(arr[nx][ny]) or (arr[x][y]<0 and abs(arr[nx][ny])!=abs(arr[x][y])):
                q.append((nx,ny))
                vistied[nx][ny]=True
                cand.append(nx)
    cand.sort(reverse = True)
    ans = cand[0]+1

    return ans



for k in range(1,K+1):
    c,d = map(int, input().split())
    c -=1
    #골렘 이동
    ans = move(c,d,k)
    is_in, x, y = ans
    #몸이 나가있음?
    if is_in:
        answer += bfs(x,y,k)
    else:
        arr =[[0]*C for _ in range(R)]
        

print(answer)