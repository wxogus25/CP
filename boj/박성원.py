import sys
import math

input = sys.stdin.readline

N = int(input())
numList = [int(input()) for _ in range(N)]
K = int(input())
dp = [[0]*K for _ in range(1<<N)]
numLen = [len(str(i)) for i in numList]
numList = [i % K for i in numList]
zeroNum = [1]
for _ in range(50):
    zeroNum.append((zeroNum[-1]*10)%K)

dp[0][0] = 1
for i in range(1<<N):
    for k in range(K):
        mod = k
        for j in range(N):
            if i & (1 << j) == 0:
                nextMod = ((mod * zeroNum[numLen[j]]) % K + numList[j]) % K
                dp[i | (1 << j)][nextMod] += dp[i][mod]

if dp[(1<<N)-1][0] == 0:
    print('0/1')
else:
    res = sum(dp[(1<<N)-1])
    gcd = math.gcd(dp[(1<<N)-1][0],res)
    print(f'{dp[(1<<N)-1][0]//gcd}/{res//gcd}')
