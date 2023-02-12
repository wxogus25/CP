import sys

input = sys.stdin.readline

T = int(input())

while T > 0:
    T -= 1

    a, b = map(int, input().split())
    n, m = map(int, input().split())

    if m*a >= (m+1)*b:
        print(n*b)
    else:
        print(n // (m + 1) * m * a + (n % (m + 1)) * min(a, b))