from collections import deque
n, k = map(int, input().split())
arr = list(map(int, input().split()))
people = [0]*len(arr)
q = deque(arr)
p = deque(people)
value = 0
answer = 0


now = 0
while value < k:
    q.rotate(1)
    p.rotate(1)

    if people[n-1] >0:
        people[n-1] = 0

    for i in range(n-2, -1, -1):
        if p[i] >0 and p[i+1] ==0 and q[i+1]>0:
            p[i+1] = p[i]
            p[i]= 0
            q[i+1] -=1
            if q[i+1] <=0:
                value +=1

    if q[0] > 0 and people[0] == 0:
        p[0] +=1
        q[0] -=1
        if q[0] <=0:
            value+=1
    answer+=1

print(answer)