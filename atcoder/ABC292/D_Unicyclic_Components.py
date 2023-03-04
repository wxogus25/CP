import sys

inp = sys.stdin.readline

N, M = map(int, inp().split())

group = [-1] * (N + 1)
edge = [0] * (N + 1)
vec = [1] * (N + 1)

def gFind(x):
    if group[x] != -1:
        group[x] = gFind(group[x])
        return group[x]
    return x

def union(a, b):
    ga = gFind(a)
    gb = gFind(b)

    if ga == gb:
        edge[ga] += 1
        return

    edge[ga] += edge[gb] + 1
    vec[ga] += vec[gb]
    group[gb] = ga
    return


while M > 0:
    M -= 1
    u, v = map(int, inp().split())

    union(u, v)

check = True

for i in range(1, N + 1):
    if group[i] == -1:
        if edge[i] != vec[i]:
            check = False
            break

print("Yes" if check else "No")