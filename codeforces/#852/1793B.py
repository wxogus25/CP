import sys
input = sys.stdin.readline

T = int(input())

def solve():
    x, y = map(int, input().split())
    
    ans = list(range(x, y - 1, -1)) + list(range(y + 1, x))
    print(len(ans))
    print(*ans)

while T > 0:
    T -= 1
    solve()