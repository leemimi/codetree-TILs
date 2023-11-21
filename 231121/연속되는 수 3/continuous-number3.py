n = int(input())
arr = [int(input()) for _ in range(n)]

res,cnt = 0,0
for i in range(n):
    if i >= 1 and arr[i]*arr[i-1]>0:
        cnt+=1
    else:
        cnt = 1
    res = max(cnt, res)

print(res)