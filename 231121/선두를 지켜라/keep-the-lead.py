n,m = map(int, input().split())
posA = [0]*1000000
posB = [0]*1000000
time = 1
for _ in range(n):
    v,t = map(int, input().split())
    for i in range(t):
        posA[time] = posA[time-1] + v
        time+=1

time1 = 1
for _ in range(m):
    v,t = map(int, input().split())
    for i in range(t):
        posB[time1] = posB[time1-1]+v
        time1 +=1

leader, ans =0,0
for i in range(1,time):
    if posA[i] > posB[i]:
        if leader == 2:
            ans+=1
        leader = 1
    elif posA[i] < posB[i]:
        if leader == 1:
            ans+=1
        leader = 2
print(ans)