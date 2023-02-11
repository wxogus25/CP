import sys

input = sys.stdin.readline

T = int(input())

while T > 0:
    T -= 1
    n = int(input())
    if n %2 == 0:
        print("No")
    else:
        print("Yes")
        ans = [[1 + x, 2*n - x] for x in range(n)]
        check = [0 for x in range(n)]
        rng = [x for x in range(n // 2, -1, -2)]
        rng_cnt = 0
        rng_len = len(rng)

        for i in range(n):
            if rng_cnt == rng_len:
                if check[i]:
                    continue
                x = n - 1
                while i < x:
                    temp = ans[i][1]
                    ans[i][1] = ans[x][1]
                    ans[x][1] = temp
                    i += 1
                    x -= 1
                break
            if not check[i]:
                check[i] = check[i + rng[rng_cnt]] = 1
                temp = ans[i][1]
                ans[i][1] = ans[i + rng[rng_cnt]][1]
                ans[i + rng[rng_cnt]][1] = temp
                rng_cnt += 1
        
        for x in ans:
            print(*x)


