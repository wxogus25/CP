import sys
import bisect

input = sys.stdin.readline

N = int(input())
dots = list(map(int, input().split()))

MOD = 10 ** 9 + 7
pow = [(2**x)%MOD for x in range(N)]
ans = 0

for l in range(N):
    i = bisect.bisect_left(dots, dots[l] * 2 - dots[l])
    j = bisect.bisect_left(dots, dots[l] * 2 - dots[l]) - 1
    left = right = dots[l]
    for r in range(l + 1, N):
        left = left + dots[r - 1] - dots[r]
        right = right - dots[r - 1] * 2 + dots[r] * 2

        while i > 0 and dots[i - 1] >= left: i -= 1
        while j < N - 1 and dots[j + 1] < right: j += 1
        
        ans += pow[N - (j - i + 1)]
        ans %= MOD

print(ans)