import sys

n = int(input())
arr = [(int(input())) for _ in range(n)]
min_dist = sys.maxsize

ns = sum(arr)

for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist+= arr[j]*((j+n-i)%n)
    min_dist = min(sum_dist,min_dist)
print(min_dist)