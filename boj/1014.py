import sys
import math

input = sys.stdin.readline

T = int(input())
H, W = 0, 0


def checkLeft(bits):
    return bool(bits & 1)


def checkUpperLeft(bits):
    return bool(bits & (1 << W))


def checkUpperRight(bits):
    return bool(bits & (1 << (W - 2)))


for _ in range(T):
    H, W = map(int, input().split())

    room = [0]*H
    for i in range(H):
        room[i] = input().rstrip()

    dp = [[[-1]*(1 << (W + 1)) for _ in range(W)] for _ in range(H)]

    dp[0][0][0] = 0
    ans = 0
    if room[0][0] == '.':
        dp[0][0][1] = 1
        ans = 1

    for i in range(H):
        for j in range(W):
            y = j - 1 if j != 0 else (W - 1)
            x = i - 1 if (y == W - 1) else i
            for k in range((1 << (W + 1))):
                if x < 0:
                    break
                if dp[x][y][k] != -1:
                    dp[i][j][(k << 1) % (1 << (W + 1))] = max(dp[i][j][(k << 1) % (1 << (W + 1))], dp[x][y][k]) # 나머지로인해 겹치는 경우 있음
                    if not ((i != 0 and j != 0 and checkUpperLeft(k)) or (i != 0 and (j != W-1) and checkUpperRight(k)) or (j != 0 and checkLeft(k)) or (room[i][j] == 'x')):
                        dp[i][j][((k << 1) + 1) % (1 << (W + 1))] = dp[x][y][k] + 1

    for k in range((1 << (W + 1))):
        ans = max(ans, dp[H-1][W-1][k])
    print(ans)
