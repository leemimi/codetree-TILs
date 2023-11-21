MAX_T = 1000000
n,m = map(int, input().split())
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)
timeA=1
for _ in range(n):
    d, t = tuple(input().split())
    for _ in range(t):
        pos_a[timeA] = pos_a[timeA-1] + (1 if d=='R' else -1)
        timeA+=1
timeB = 1
for _ in range(m):
    d, t = tuple(input().split())
    for _ in range(t):
        pos_b[timeB] = pos_b[timeB-1] + (1 if d=='R' else -1)
        timeB +=1

ans = -1
for i in range(1,timeA):
    if pos_a[i] == pos_b[i]:
        ans = i
        break
print(ans)