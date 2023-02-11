import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))

cnt = 0
stack = []

for i in range(1, N + 1):
    if cnt < M and i == numList[cnt]:
        stack.append(i)
        cnt += 1
        continue
    stack.append(i)
    stack.reverse()
    print(*stack, end = ' ')
    stack.clear()