import sys
inp = sys.stdin.readline

T = int(inp())

while T > 0:
    T -= 1
    N, M = map(int, inp().split())
    p = list(map(int, inp().split()))

    check = [0] * (N + M + 1)
    lst = [0] * N
    ans = [-1] * (N + 1)

    for x in range(1, N + 1):
        check[x] = 1
        lst[x - 1] = N - x + 1

    pivot = 0
    cnt = 0
    for x in p:
        cnt += 1
        if check[x] == 0:
            check[lst[pivot % N]] = 0
            check[x] = 1
            if lst[pivot % N] <= N:
                ans[lst[pivot % N]] = cnt
            lst[pivot % N] = x
            pivot += 1
    
    for i in range(1, N + 1):
        print(ans[i], end = ' ')
    print()