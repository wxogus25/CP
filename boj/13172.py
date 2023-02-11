N = int(input())
_mod = 1000000007


def pow(a, b):
    if b == 1:
        return a
    if b % 2 == 1:
        return ((((pow(a, b//2) % _mod)**2) % _mod) * a) % _mod
    else:
        return ((pow(a, b//2) % _mod)**2) % _mod


sum = 0
for i in range(N):
    n, s = map(int, input().split())
    sum += (s * pow(n, _mod - 2)) % _mod

print(sum)
