import sys

input = sys.stdin.readline

T = int(input())

while T > 0:
    T -= 1
    N = int(input())
    d = list(map(int,input().split()))
    a = 1
    b = 1
    for x in d:
        a *= x
    ans = -1
    for x in range(N):
        b *= d[x]
        a /= d[x]
        if b == a:
            ans = x + 1
            break
    if ans == -1:
        print(-1)
    else:
        print(ans)
