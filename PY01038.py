def check(n):
    res = 0
    if int(n) % 7 == 0:
        return int(n)
    for i in range(1000):
        res = int(n) + int(n[::-1])
        if res % 7 == 0:
            return res
        n = str(res)
    return -1

t = int(input())
while t > 0:
    t -= 1
    print(check(input()))