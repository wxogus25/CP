import sys
input = sys.stdin.readline

T = int(input())

while T>0:
    T -= 1
    N = int(input())
    aList = list(map(int, input().split()))
    aList.insert(0, 0)


    mn = 10000000
    mx = 0
    for i in range(1, N+1):
        if aList[aList[i]] == i and aList[i] != i:
            mn = min(mn, aList[i])
            mx = max(mx, aList[i])
    
    if mx - mn >= 3:
        print(f'{mn} {mx}')
    else:
        print(-1)