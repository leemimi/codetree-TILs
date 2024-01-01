n,m = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(n)]

res = 0
for i in range(n-1):
    cnt= 0
    cnt1=0
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1]:
            cnt+=2
        if arr[j][i] == arr[j][i+1]:
            cnt1+=2
    if cnt >= m or cnt1 >= m:
        res +=1
print(res)