from cmath import inf

N, M, R = map(int, input().split())
graph = [[inf for _ in range(N+1)] for _ in range(N+1)]
items = list(map(int, input().split()))
items[0:0] = [0]
for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a][b] = graph[b][a] = l

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                continue 
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


def ans(now):
    answer = items[now]
    for (i, x) in enumerate(graph[now]):
        if x <= M:
            answer += items[i]
    return answer


print(max(map(ans, range(1, N+1))))
