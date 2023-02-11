import sys
from cmath import inf
from queue import Queue

input = sys.stdin.readline

T = int(input())

def bfs(st, ed, edge, colors, stcolor):
    arr = [inf] * (max(st, ed) + 1)

    que = Queue()
    que.put(st)
    arr[st] = 0
    while not que.empty():
        now = que.get()
        if now == ed:
            break   
        for x in edge[now]:
            if arr[x] == inf and colors[x] == (stcolor ^ (arr[now] % 2)):
                arr[x] = arr[now] + 1
                que.put(x)
    
    print(arr)
    
    return arr[ed]
    
for t in range(T):
    N, M = map(int, input().split())
    colors = list(map(int, input().split()))
    colors.insert(0, -1)
    edge = [[] for i in range(N + 1)]
    for i in range(M):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)

    ztov0 = bfs(1, N, edge, colors, 0)
    vtoz1 = bfs(N, 1, edge, colors, 1)
    ztov1 = bfs(1, N, edge, colors, 1)
    vtoz0 = bfs(N, 1, edge, colors, 0)

    if ztov0 == vtoz1 != inf:
        if ztov1 == vtoz0 != inf and ztov1 < ztov0:
            print(ztvo1)
        else:
            print(ztov0)
    elif ztov1 == vtoz0 != inf:
        if ztov0 == vtoz1 != inf and ztov0 < ztov1:
            print(ztov0)
        else:
            print(ztov1)
    else:
        print(-1)
    