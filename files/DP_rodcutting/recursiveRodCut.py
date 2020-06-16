debug = False
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def rodcut(n):
    if debug: print('n:',n)
    if n == 0:
        return 0
    max = -9999999999
    for i in range(0,n):
        if debug: print('n:',n,'i:',i)
        tmp = rodcut(n-i-1)
        max_tmp = p[i] + tmp
        if debug: print('max tmp:', max_tmp,'rodcut(n-i):',tmp)
        if max < max_tmp:
            max = max_tmp
    return max

# mian
rodSize = int(input('Plz input a number between 1 and 10 as rod size:'))
result = rodcut(rodSize)
print(result)