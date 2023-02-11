import sys
import math

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, W = map(int, input().split())
    section = [0] * 2
    for k in range(2):
        section[k] = list(map(int, input().split()))
    section[0].append(section[0][0])
    section[1].append(section[1][0])

    # 0, 1, 2, 3 : k(시작 상태)

    dp = [[[0]*4 for _ in range(N)] for _ in range(4)]
    for k in range(4):
        if k == 0:
            dp[k][0][0] = 2 if (section[0][0] + section[1][0] > W) else 1
            dp[k][0][1] = 3 if (section[0][0] + section[0][1] > W) else 2
            dp[k][0][2] = 3 if (section[1][0] + section[1][1] > W) else 2
            dp[k][0][3] = (2 if (section[0][0] + section[0][1] > W) else 1) + \
                (2 if (section[1][0] + section[1][1] > W) else 1)
        elif k == 1:
            dp[k][0][0] = 1
            dp[k][0][1] = 2
            dp[k][0][2] = 2 if (section[1][0] + section[1][1] > W) else 1
            dp[k][0][3] = 3 if (section[1][0] + section[1][1] > W) else 2
        elif k == 2:
            dp[k][0][0] = 1
            dp[k][0][1] = 2 if (section[0][0] + section[0][1] > W) else 1
            dp[k][0][2] = 2
            dp[k][0][3] = 3 if (section[0][0] + section[0][1] > W) else 2
        else:
            dp[k][0][0] = 0
            dp[k][0][1] = 1
            dp[k][0][2] = 1
            dp[k][0][3] = 2

        for i in range(1, N):
            dp[k][i][0] = min(
                (dp[k][i-1][0] + (2 if (section[0][i] + section[1][i] > W) else 1)),
                (dp[k][i-1][1] + 1),
                (dp[k][i-1][2] + 1),
                (dp[k][i-1][3]),
            )
            dp[k][i][1] = min(
                (dp[k][i-1][0] + (3 if (section[0][i] + section[0][i+1] > W) else 2)),
                (dp[k][i-1][1] + 2),
                (dp[k][i-1][2] + (2 if (section[0][i] + section[0][i+1] > W) else 1)),
                (dp[k][i-1][3] + 1),
            )
            dp[k][i][2] = min(
                (dp[k][i-1][0] + (3 if (section[1][i] + section[1][i+1] > W) else 2)),
                (dp[k][i-1][1] + (2 if (section[1][i] + section[1][i+1] > W) else 1)),
                (dp[k][i-1][2] + 2),
                (dp[k][i-1][3] + 1),
            )
            dp[k][i][3] = min(
                (dp[k][i-1][0] + ((2 if (section[0][i] + section[0][i+1] > W)
                 else 1) + (2 if (section[1][i] + section[1][i+1] > W) else 1))),
                (dp[k][i-1][1] + (3 if (section[1][i] + section[1][i+1] > W) else 2)),
                (dp[k][i-1][2] + (3 if (section[0][i] + section[0][i+1] > W) else 2)),
                (dp[k][i-1][3] + 2),
            )
    print(min(dp[x][N-1][x] for x in range(4)))
