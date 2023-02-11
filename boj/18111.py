import sys
import math
input = sys.stdin.readline

M, N, B = map(int, input().split())
ground = [0] * M

for i in range(M):
    ground[i] = list(map(int, input().split()))


def func(high):
    block = B
    cost = 0
    for i in range(M):
        for j in range(N):
            if ground[i][j] > high:
                cost += (ground[i][j] - high)*2
                block += ground[i][j] - high
            elif ground[i][j] < high:
                cost += high - ground[i][j]
                block -= high - ground[i][j]

    if block < 0:
        return math.inf
    else:
        return cost


answer = (math.inf, 257)

for i in range(256, -1, -1):
    cost = func(i)
    if cost < answer[0]:
        answer = (cost, i)

print(f'{answer[0]} {answer[1]}')
