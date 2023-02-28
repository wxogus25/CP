import sys
inp = sys.stdin.readline

T = int(inp())

while T > 0:
    T -= 1
    N = int(inp())
    lst = list(map(int, inp().split()))

    minn = min(lst)
    maxx = max(lst)
    ans = []

    if minn == 1:
        if maxx == 1:
            print(0)
        else:
            print(-1)
    elif minn == maxx:
        print(0)
    else:
        idxn = 0
        for i in range(N):
            if lst[i] == minn:
                idxn = i
                break
        idx = 0
        while not(idx == 0 and minn == maxx):
            if idx == 0:
                maxx = lst[idx]

            if lst[idx] > minn:
                lst[idx] = lst[idx] // minn + (1 if lst[idx] % minn != 0 else 0)
                ans.append((idx + 1, idxn + 1))
                maxx = max(maxx, lst[idx])
                if lst[idx] < minn:
                    minn = lst[idx]
                    idxn = idx
            idx = (idx + 1) % N
        
        print(len(ans))
        for x in ans:
            print(f'{x[0]} {x[1]}')

