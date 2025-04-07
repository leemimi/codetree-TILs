from collections import deque
n,m,K = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]
people = [list(map(int, input().split()))for _ in range(m)]
ex, ey = map(int, input().split())
ex -=1
ey -=1
answer = 0
cnt = m

#좌표 맞춰주기

for p in range(m):
    people[p][0] -=1
    people[p][1] -=1
    arr[people[p][0]][people[p][1]] -= 1
#출구
arr[ex][ey] = -11


#한명이상 참가자와 정사각형 찾기
def find_square(arr):
    # [1] 비상구와 모든 사람간의 가장짧은 가로 또는 세로거리 구하기 => L
    mn = n
    for i in range(n):
        for j in range(n):
            if -11<arr[i][j]<0:     # 사람인 경우
                mn=min(mn, max(abs(ei-i), abs(ej-j)))

    # [2] (0,0)부터 순회하면서 길이 L인 정사각형에 비상구와 사람있는지 체크 => 리턴 L+1
    for si in range(n-mn):
        for sj in range(n-mn):                  # 가능한 모든 시작위치
            if si<=ei<=si+mn and sj<=ej<=sj+mn: # 비상구가 포함된 사각형!
                for i in range(si, si+mn+1):
                    for j in range(sj, sj+mn+1):
                        if -11<arr[i][j]<0:     # 사람인 경우 리턴!
                            return si,sj,mn+1

def find_exit():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == -11:
                return i,j

for _ in range(K):
    #참가자들 이동
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
                            cnt-=1
                        else:
                            tmp[nx][ny]+=arr[i][j]
                        break
    arr = tmp

    if cnt == 0:
        break

    a,b,lenz = find_square(arr)

    tmp = [x[:] for x in arr]
    for i in range(lenz):
        for j in range(lenz):
            tmp[a+i][b+j] = arr[a+lenz-1-j][b+i]
            if tmp[a+i][b+j] > 0:
                tmp[a+i][b+j] -=1
    
    arr = tmp
    #출구찾기
    ex,ey = find_exit()


print(-answer)
print(ex+1,ey+1)