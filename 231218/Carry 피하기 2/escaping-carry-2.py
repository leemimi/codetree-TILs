n = int(input())
arr = [int(input()) for _ in range(n)]

def check(a,b,c):
    result = a+b+c

    while a!=0 or b!=0 or c!=0:
        if 10<= a%10 + b%10 +c%10 :
            return -1
        a,b,c = a//10,b//10,c//10
    return result


ans = -1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            ans = max(ans, check(arr[i],arr[j],arr[k]))
print(ans)