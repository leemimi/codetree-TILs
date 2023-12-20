n = int(input())
arr = list(map(int, input().split()))
mx = sum(arr)
for i in range(n):
    arr[i] *=2
    for j in range(n):
        rm = []
        for k, e in enumerate(arr):
            if k!=j:
                rm.append(arr[k])
        diff = 0
        for k in range(n-2):
            diff += abs(rm[k+1]-rm[k])
        mx = min(mx, diff)
    arr[i] //=2
print(mx)