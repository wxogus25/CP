import sys
input = sys.stdin.readline

N = int(input())
chu = list(map(int, input().split()))
T = int(input())
mooge = list(map(int, input().split()))

check = [0] * 80001
check[0] = 1

for x in chu:
    for i in range(80000, x - 1, -1):
        if i - x <= 80000 and check[i - x]:
            check[i] = 1

for x in mooge:
    ck = 0
    for i in range(80001):
        if check[i] and i + x <= 80000 and check[i + x]:
            ck = 1
            break
    print('NY'[ck], end = ' ')
