n,m,k = map(int, input().split())
student = [0]*(1+n)
res = -1
for _ in range(m):
    c = int(input())
    student[c] +=1
    if student[c] >=k:
        res = c
        break
print(res)