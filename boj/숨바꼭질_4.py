import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
check = [-1] * 200000
tracking = [-1] * 200000
queue = deque([N])
check[N] = 0

while queue:
    now = queue.popleft()
    if now == K:
        break
    if now * 2 < 200000 and check[now * 2] == -1:
        check[now * 2] = check[now] + 1
        tracking[now * 2] = now
        queue.append(now * 2)
    if now + 1 >= 0 and now + 1 < 200000 and check[now + 1] == -1:
        check[now + 1] = check[now] + 1
        tracking[now + 1] = now
        queue.append(now + 1)
    if now - 1 >= 0 and now - 1 < 200000 and check[now - 1] == -1:
        check[now - 1] = check[now] + 1
        tracking[now - 1] = now
        queue.append(now - 1)

print(check[K])

x = K
ans = []
while x != -1:
    ans.append(x)
    x = tracking[x]

ans.reverse()
print(*ans)