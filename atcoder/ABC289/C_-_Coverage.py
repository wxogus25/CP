import sys

input = sys.stdin.readline

N, M = map(int, input().split())
c = []

for i in range(M):
    _=input()
    c.append(list(map(int, input().split())))


res = 0

for i in range(2**M):
    s = set()

    cnt = 0
    while 1 << cnt <= i:
        if (1 << cnt) & i:
            s.update(c[cnt])
        cnt += 1
    

    if len(s) == N:
        res += 1

print(res)