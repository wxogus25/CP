import sys
from cmath import inf
inp = sys.stdin.readline

N = int(inp())
M = int(inp())

d = [[inf for i in range(N + 1)] for j in range(N + 1)]
pre = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in range(M):
    x, y, c = map(int, inp().split())
    d[x][y] = min(d[x][y], c)
    pre[x][y] = y

for k in range(1, N + 1):
    for i in range(1, N + 1):
        if i == k: continue
        for j in range(1, N + 1):
            if i == j: continue
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
                pre[i][j] = pre[i][k]


for i in range(1, N + 1):
    for j in range(1, N + 1):
        if d[i][j] == inf:
            d[i][j] = 0

for x in range(1, N + 1):
    print(*d[x][1:])

def tracking(st, ed):
    ans = [st]
    while pre[st][ed] != 0:
        ans.append(pre[st][ed])
        st = pre[st][ed]
    return ans


for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j or d[i][j] == 0:
            print(0)
        else:
            ans = tracking(i, j)
            print(len(ans), end = ' ')
            print(*ans)