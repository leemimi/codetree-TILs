n = int(input())
arr = [list(map(int,input().split()))for _ in range(n)]

def solve(x1,y1,x2,y2):
    cnt = 0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            cnt += arr[i][j]
    return cnt

answer = 0
for i in range(n):
    for j in range(n):
        if i+2 >=n or j+2 >= n:
            continue
        cnt = solve(i,j,i+2,j+2)
        answer = max(cnt, answer)
print(answer)