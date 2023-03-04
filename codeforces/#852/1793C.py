import sys
input = sys.stdin.readline

T = int(input())

def solve():
    N = int(input())
    aList = list(map(int, input().split()))
    cList = [1] * N

    cst = st = 0
    ced = ed = N - 1
    check = False

    while ed - st >= 3:
        while cList[cst] == 0: cst += 1
        while cList[ced] == 0: ced -= 1

        ck1 = min(aList[st], aList[ed]) != cst + 1
        ck2 = max(aList[st], aList[ed]) != ced + 1

        if ck1 and ck2:
            check = True
            break
        elif ck1 and not ck2:
            if aList[st] == ced + 1:
                cList[aList[st]-1] = 0
                st += 1
            else:
                cList[aList[ed]-1] = 0
                ed -= 1
        elif ck2 and not ck1:
            if aList[st] == cst + 1:
                cList[aList[st]-1] = 0
                st += 1
            else:
                cList[aList[ed]-1] = 0
                ed -= 1
        else:
            cList[aList[st]-1] = cList[aList[ed]-1] = 0
            st += 1
            ed -= 1


    if check:
        print(f'{st + 1} {ed + 1}')
    else:
        print(-1)

while T>0:
    T -= 1
    solve()
    