import sys
input = sys.stdin.readline

T = int(input())

def check(X):
    lenX = len(X)
    for i in range(1, lenX):
        if X[i-1] == X[i]:
            return False
    
    return True

while T > 0:
    T -= 1
    N, M = map(int, input().split())
    A = input().rstrip()
    B = input().rstrip()

    if check(A) and check(B):
        print("YES")
    elif not check(A) and not check(B):
        print("NO")
    elif not check(A) and check(B):
        Bs = B
        ck = False
        lenA = len(A)
        for i in range(lenA - 1, 0, -1):
            temp = A[i:]
            As = A[0:i]
            Bs += temp[::-1]
            if check(As) and check(Bs):
                ck = True
                break
            Bs = B
        
        print("YES" if ck else "NO")
    else:
        As = A
        ck = False
        lenB = len(B)
        for i in range(lenB - 1, 0, -1):
            temp = B[i:]
            Bs = B[0:i]
            As += temp[::-1]
            if check(As) and check(Bs):
                ck = True
                break
            As = A

        print("YES" if ck else "NO")
    