import sys

input = sys.stdin.readline

N = input().rstrip()

ans = [0]*10
exp = 10**(len(N)-1)

for k in range(len(N)):
    x = int(N[k])
    for i in range(0, x):
        ans[i] += exp
    ans[x] += (int(N) % exp) + 1

    for j in range(10):
        ans[j] += exp * (int(N) // (exp*10))
    ans[0] -= exp
    exp //= 10
    
print(" ".join(list(map(str,ans))))