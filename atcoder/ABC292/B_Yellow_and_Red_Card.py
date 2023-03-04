import sys

inp = sys.stdin.readline

N, Q = map(int, inp().split())

players = [0] * 101

while Q > 0:
    Q -= 1
    c, x = map(int, inp().split())

    if c == 1:
        players[x] += 1
    elif c == 2:
        players[x] += 2
    else:
        print("Yes" if players[x] >= 2 else "No")