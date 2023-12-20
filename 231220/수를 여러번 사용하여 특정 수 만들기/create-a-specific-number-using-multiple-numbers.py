A,B,C = map(int, input().split())

ans = set()
for i in range(C//A+1):
    a = A*i
    for j in range(C//B+1):
        b = B*j
        if a+b <= C:
            ans.add(a+b)

print(max(ans))