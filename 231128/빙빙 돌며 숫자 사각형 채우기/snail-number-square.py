n,m = map(int, input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]
x,y = 0,0
arr = [[0]*m for _ in range(n)]
arr[0][0] = 1
visited = [[False]*m for _ in range(n)]
dir = 0
for i in range(2,n*m+1):
    nx,ny = x+dx[dir], y+dy[dir]
    if not (0<=nx<n and 0<=ny<m) or arr[nx][ny]!=0:
        dir = (dir+1)%4  
    x,y = x+dx[dir],y+dy[dir]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()