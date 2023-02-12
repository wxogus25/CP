from cmath import inf
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
p = [(0, i) for i in range(N)]
p[0] = (arr[0], 0)

for i in range(1, N):
    p[i] = (p[i-1][0] + arr[i], i)

for i in range(N):
    dp[i] = i + 1 if p[i][0] >= 0 else 0

p.sort(key=lambda x: (x[0], x[1]))
rank = [0]*N
for i in range(N):
    rank[p[i][1]] = i

tree = [-inf] * (2 * N)


def rngSolve(l, r):
    res = -inf
    l += N
    r += N

    while l < r:
        if l & 1:
            res = max(res, tree[l])
            l += 1
        if r & 1:
            r -= 1
            res = max(res, tree[r])
        l >>= 1
        r >>= 1

    return res


def update(index, value):
    tree[N + index] = value
    index += N
    while index > 1:
        tree[index >> 1] = max(tree[index], tree[index ^ 1])
        index >>= 1


update(rank[0], dp[0])
for i in range(1, N):
    dp[i] = max(dp[i], dp[i-1], rngSolve(0, rank[i] + 1) + i)
    update(rank[i], dp[i] - i)


print(dp[N-1])
