import sys

input = sys.stdin.readline

T = int(input())


for x in range(T):
    n = int(input())
    
    x = str(n)
    a = b = 0
    an = bn = 0
    for c in x:
        a += int(c) // 2
        b += int(c) // 2
        an += int(c)
        bn += int(c)

        if an > bn:
            b += int(c) % 2
            bn += int(c) % 2
        else:
            a += int(c) % 2
            an += int(c) % 2
        
        a *= 10
        b *= 10
    
    a //= 10
    b //= 10
    print(f'{a} {b}')