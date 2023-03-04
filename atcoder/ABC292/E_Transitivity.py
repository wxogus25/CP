import sys
from cmath import inf
from collections import deque

inp = sys.stdin.readline
N, M = map(int, inp().split())

edges = [[] for i in range(N + 1)]

while M > 0:
    M -= 1
    u, v = map(int, inp().split())
    edges[u].append(v)


def bfs(start):
    level = [inf] * (N + 1)
    level[start] = 0
    queue = deque([start])

    while queue:
        now = queue.popleft()
        for x in edges[now]:
            if level[x] == inf:
                level[x] = level[now] + 1
                queue.append(x)
    
    ans = 0

    for x in level:
        if x != inf and x > 1:
            ans += 1

    return ans

ans = 0

for i in range(1, N + 1):
    ans += bfs(i)

print(ans)