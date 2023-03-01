import sys

inp = sys.stdin.readline

T = int(inp())

while T > 0:
    T -= 1
    A = inp().rstrip()
    B = inp().rstrip()
    lenA = len(A)
    lenB = len(B)

    LCS = [[0 for i in range(100)] for j in range(100)]

    maxx = 0
    idxm = -1

    for i in range(lenA + 1):
        for j in range(lenB + 1):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            elif A[i-1] == B[j-1]:
                LCS[i][j] = 1 if i < 1 or j < 1 else LCS[i-1][j-1] + 1
                if LCS[i][j] > maxx:
                    maxx = LCS[i][j]
                    idxm = i - 1

    lcs = []

    for i in range(maxx):
        lcs.append(A[idxm-i])

    lcs.reverse()
    
    lenL = len(lcs)

    if lenL > 1:
        print("YES")
        print(f'*{"".join(lcs)}*')
    elif A[0] == B[0]:
        print("YES")
        print(f'{A[0]}*')
    elif A[-1] == B[-1]:
        print("YES")
        print(f'*{A[-1]}')
    else:
        print("NO")
