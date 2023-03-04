import sys

inp = sys.stdin.readline

N = int(inp())

ans = 0

for a in range(1, N // 2 + 1):
    tempa = 0
    tempb = 0
    b = N - a
    for i in range(1, int(a**(1/2)) + 1):
        if (a % i == 0):
            tempa += 1
            if ((i**2) != a):
                tempa += 1
    
    for i in range(1, int(b**(1/2)) + 1):
        if (b % i == 0):
            tempb += 1
            if ((i**2) != b):
                tempb += 1

    if a == b:
        ans += tempa * tempb
    else:
        ans += tempa * tempb * 2

print(ans)