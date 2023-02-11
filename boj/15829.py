import sys
input = sys.stdin.readline

N = int(input())
string = input().rstrip()

result = 0
r = 1

for x in string:
    result += (ord(x)-96)*r
    r *= 31
    result %= 1234567891

print(result)
