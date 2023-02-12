import sys
import bisect

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

lis = [seq[0]]
sList = [0]
tracking = [-1]*N

length = 1

for i in range(1, N):
    x = bisect.bisect_left(lis, seq[i])
    if x == length:
        tracking[i] = sList[x - 1]
        lis.append(seq[i])
        sList.append(i)
        length += 1
    else:
        if x == 0:
            tracking[i] = -1
            lis[x] = seq[i]
            sList[x] = i
        else:
            tracking[i] = sList[x - 1]
            lis[x] = seq[i]
            sList[x] = i

print(length)

def track(x):
    trace = []
    while x != -1:
        trace.append(seq[x])
        x = tracking[x]
    return trace

ans = track(sList[length - 1])
ans.reverse()
print(*ans)