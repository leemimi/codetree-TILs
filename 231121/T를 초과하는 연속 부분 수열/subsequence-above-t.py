n,t = map(int,input().split())
arr = list(map(int,input().split()))

res,cnt = 0,0
for i in range(n):
    if t<arr[i-1]<arr[i]:        
        cnt+=1
    else:
        cnt = 0
    res = max(cnt, res)
print(res)