import sys
input = sys.stdin.readline

T = int(input())

def check(X, k):
    if X[k] == max(X) and X.count(max(X)) == 1:
        return True
    return False

while T > 0:
    T -= 1
    N, K = map(int, input().split())
    I = [0] * 51
    for x in range(N):
        l, r = map(int, input().split())
        if l <= K <= r:
            for i in range(l, r+1, 1):
                I[i] += 1
    if check(I, K):
        print("YES")
    else:
        print("NO")    