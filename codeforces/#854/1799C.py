import sys
inp = sys.stdin.readline

T = int(inp())

while T > 0:
    T -= 1
    s = inp().rstrip()
    cnt = [0] * 26

    for x in s:
        cnt[ord(x) - ord('a')] += 1
    
    diff = 0
    for i in range(26):
        if cnt[i] > 0:
            diff += 1
    
    if diff == 1:
        print(s)
    elif diff == 2:
        n = len(s)
        temp = [0] * n
        idx = 0
        for i in range(26):
            while cnt[i] > 1:
                temp[idx] = temp[n - idx - 1] = chr(ord('a') + i)
                cnt[i] -= 2
                idx += 1
        ck = 0
        for i in range(26):
            if cnt[i] > 0:
                temp[idx] = chr(ord('a') + i)
                if ck == 0:
                    idx = n - idx - 1
                    ck = 1
                else:
                    ck = 0
                    idx = n - idx - 1
                    idx += 1
        temp.reverse()
        print(''.join(temp))
    else:
        n = len(s)
        temp = [0] * n
        st = 0
        ed = n - 1
        for i in range(26):
            if st != n - ed - 1 and cnt[i] > 0:
                if st > n - ed - 1:
                    temp[ed] = chr(ord('a') + i)
                    ed -= 1
                else:
                    temp[st] = chr(ord('a') + i)
                    st += 1
                cnt[i] -= 1
            

            if st != 0 and ed != n - 1:
                if ord(temp[st - 1]) > ord(temp[ed + 1]):
                    for j in range(25, -1, -1):
                        while cnt[j] > 0:
                            temp[ed] = chr(ord('a') + j)
                            cnt[j] -= 1
                            ed -= 1
                    break
                elif ord(temp[st - 1]) < ord(temp[ed + 1]):
                    for j in range(25, -1, -1):
                        while cnt[j] > 0:
                            temp[st] = chr(ord('a') + j)
                            cnt[j] -= 1
                            st += 1
                    break


            while cnt[i] > 1:
                temp[st] = temp[ed] = chr(ord('a') + i)
                cnt[i] -= 2
                st += 1
                ed -= 1

            if cnt[i] == 1:
                if st != 0 and ed != n - 1:
                    if ord(temp[st - 1]) < ord(temp[ed + 1]):
                        temp[ed] = chr(ord('a') + i)
                        ed -= 1
                    else:
                        temp[st] = chr(ord('a') + i)
                        st += 1
                else:
                    temp[st] = chr(ord('a') + i)
                    st += 1
                cnt[i] -= 1
        
        temp.reverse()
        print(''.join(temp))
