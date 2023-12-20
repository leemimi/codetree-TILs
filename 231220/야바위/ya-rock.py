n = int(input())

max_score = 0
commands = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
for i in range(1,4):
    y = [0] * 4
    y[i] = 1

    score = 0

    for a,b,c in commands:
        y[a],y[b] = y[b],y[a]

        if y[c]:
            score+=1
    max_score = max(max_score,score)

print(max_score)