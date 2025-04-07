from collections import deque
n,m,K = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]
people = [list(map(int, input().split()))for _ in range(m)]
ex, ey = map(int, input().split())
ex -=1
ey -=1
answer = 0
sx,sy = 0,0
lens = n*n
cnt = 0

#좌표 맞춰주기

for p in range(m):
    people[p][0] -=1
    people[p][1] -=1
    arr[people[p][0]][people[p][1]] -= 1
#출구
arr[ex][ey] = -11

def go_people():
    global ex,ey,answer,arr,cnt
    tmp = [x[:] for x in arr]
    for i in range(n):
        for j in range(n):
            if -11 <arr[i][j]<0:
                dist = abs(ex-i) + abs(ey-j)
                for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                    nx = i+di
                    ny = j +dj
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny]<=0 and dist>(abs(ex-nx)+abs(ey-ny)):
                        answer += arr[i][j]
                        tmp[i][j] -= arr[i][j]
                        if arr[nx][ny] == -11:
                            cnt+=1
                        else:
                            tmp[nx][ny]+=arr[i][j]
                        break
    arr = tmp

    
#한명이상 참가자와 정사각형 찾기
def find_square(arr):
    global ex,ey

    #1.사람과 탈출구간의 짧은 거리를 구함
    min_len = n
    for i in range(n):
        for j in range(n):
            if -11 < arr[i][j] <=-1:
                min_len = min(min_len, max(abs(ex-i),abs(ey-j)))
    #2.그 짧은 거리에서 사람과 탈출구가 있니?
    for si in range(n-min_len):
        for sj in range(n-min_len):
            if si<=ex<=si+min_len and sj<=ey<=sj+min_len:
                for i in range(si, si+min_len+1):
                    for j in range(sj, sj+min_len+1):
                        if -11 < arr[i][j] < 0:
                            return si,sj,min_len+1

def find_exit():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == -11:
                ex = i
                ey = j
                return i,j

for _ in range(K):
    #참가자들 이동
    go_people()

    if cnt == m:
        break

    a,b,lens = find_square(arr)

    tmp = [x[:] for x in arr]
    for i in range(lens):
        for j in range(lens):
            tmp[a+i][b+j] = arr[a+lens-1-j][b+i]
            if tmp[a+i][b+j] > 0:
                tmp[a+i][b+j] -=1
    
    arr = tmp
    #출구찾기
    ex,ey = find_exit()


print(-answer)
print(ex+1,ey+1)