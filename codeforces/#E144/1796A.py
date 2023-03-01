import sys

inp = sys.stdin.readline

T = int(inp())

while T > 0:
    T -= 1
    N = int(inp())
    s = inp().rstrip()
    t = "FBFFBFFBFBFFBFFBFBFFBFFB"

    if s in t:
        print("YES")
    else:
        print("NO")
