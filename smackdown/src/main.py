import heapq
from collections import defaultdict

lines = None


def myinput():
    global lines
    if lines is None:
        lines = [it.strip() for it in open("../in.txt").readlines()]
    tmp = lines[0]
    lines = lines[1:]
    return tmp


# =====================
# input = myinput


def solve():
    n, k = map(int, input().split())
    # aa = [int(it) for it in input().split()]
    if k * (k + 1) // 2 > n:
        print("-1")
        return
    a = int(n / k - (k - 1) / 2)
    more_to_move = n - sum(range(a,a+k))
    res = 1
    def mul(f):
        nonlocal res
        res *= f
        res %= 10**9+7
    n_stay = k-more_to_move
    for i in range(a,a+n_stay):
        mul(i)
        mul(i-1)
    for i in range(a+n_stay+1,a+k+1):
        mul(i)
        mul(i-1)
    print(res)


# ======================
T = int(input().strip())
for tid in range(1, 1 + T):
    solve()
