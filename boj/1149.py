N = int(input())
home = []
for i in range(N):
    home.append(list(map(int, input().split())))

dp = []
dp.append(home[0])
for i in range(1, N):
    dp.append(home[i])
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + dp[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + dp[i][j]
        else:
            dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + dp[i][j]

print(min(dp[N-1]))
