from collections import deque
n, k = map(int, input().split())
arr = list(map(int, input().split()))
q = deque(arr)
p = deque([0 for i in range(2 * n)])
value = 0
answer = 0

while value < k:
    q.appendleft(q.pop())
    p.appendleft(p.pop())
    if p[n-1] > 0:
        p[n-1] = 0

    for i in range(n-1, 0, -1):
        if p[i] == 0 and p[i-1] > 0 and q[i-1]>0:
            p[i] = 1
            p[i-1]=0
            q[i] -=1
            if q[i] ==0:
                value +=1
    if p[n-1] > 0:
        p[n-1] = 0

    if q[0]:
        p[0] = 1
        q[0] -=1
        if q[0] ==0:
            value+=1
    answer+=1

print(answer)