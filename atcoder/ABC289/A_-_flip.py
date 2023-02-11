import sys

input = sys.stdin.readline

x = input().rstrip()

for i in x:
    print(1 - int(i), end='')