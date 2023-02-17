import sys
import bisect

input = sys.stdin.readline

T = int(input())

while T > 0:
    T -= 1
    N = int(input())
    tea = list(map(int, input().split()))
    tester = list(map(int, input().split()))
    psum = [0] * N
    psum[0] = tester[0]
    for i in range(1, N):
        psum[i] = psum[i-1] + tester[i]

    rsum = [0] * N
    rsum[N-1] = tester[N - 1]
    for i in range(N - 2, -1, -1):
        rsum[i] = rsum[i + 1] + tester[i]

    rsum.reverse()

    zeroTime = [[] for i in range(N)]

    for i in range(N):
        c = bisect.bisect_left(psum, tea[i] + (0 if i == 0 else psum[i - 1]))
        if c != N:
            zeroTime[c].append(i)

    cnt = 0
    rsum.reverse()
    for i in range(N):
        now = 0
        if zeroTime[i]:
            for x in zeroTime[i]:
                now += tea[x] - (rsum[x] - rsum[i])
                cnt -= 1
        cnt += 1
        now += tester[i] * cnt
        print(now, end = ' ')
    print('')
