a = [0] * 6

maxd = 0
for i in range(1, 501):
    for x in range(1, 7):
        if i % x == 0:
            a[x - 1] += 1
            a[x - 1] %= 63
        b = list(sorted(a))
        d = min(b[it + 1] - b[it] for it in range(5))
        if d > maxd:
            maxd = d
    if d >= 7 and max(b) < 62-7:
        print(i, d, b, a)
