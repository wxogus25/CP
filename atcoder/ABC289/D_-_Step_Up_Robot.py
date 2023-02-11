import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

st = [0] * (X + 1)
st[0] = 1

for x in B:
    st[x] = -1

for i in range(X):
    if st[i] == 1:
        for j in range(N):
            if i + A[j] <= X and st[i + A[j]] != -1:
                st[i + A[j]] = 1

if st[X]:
    print("Yes")
else:
    print("No")
