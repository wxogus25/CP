import sys
from collections import deque


def bfs(graph, start, V):
    visited = [0 for _ in range(V+1)]
    result = (0, 0)
    queue = deque([(start, 0)])

    while queue:
        n = queue.popleft()
        if visited[n[0]] == 0:
            visited[n[0]] = 1
            for x in graph[n[0]]:
                if visited[x[0]] == 0:
                    queue.append((x[0], x[1] + n[1]))
                    if result[1] < x[1] + n[1]:
                        result = (x[0], x[1] + n[1])

    return result


V = int(input())
E = [[] for _ in range(V+1)]

for i in range(V):
    check = list(map(int, sys.stdin.readline().split()[:-1]))
    for k in range(1, len(check), 2):
        E[check[0]].append((check[k], check[k+1]))

c = bfs(E, 1, V)
print(bfs(E, c[0], V)[1])
