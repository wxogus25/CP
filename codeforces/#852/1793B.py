import sys
input = sys.stdin.readline

T = int(input())

while T > 0:
    T -= 1
    x, y = map(int, input().split())

    dir = x // abs(x)
    N = (x - y)*2
    now = 0
    print(N)
    for i in range(N):
        print(now, end = ' ')
        if now == x:
            dir *= -1
        elif now == y:
            dir *= -1
        now += dir
    print('')