n,t = map(int,input().split())
arr = list(map(int,input().split()))

res,cnt = 0,0
for i in range(n):
    if arr[i-1] > t and arr[i] > t:
        if i>=1 and arr[i-1]<arr[i]:        
            cnt+=1
        else:
            cnt = 1
    res = max(cnt, res)
print(res)