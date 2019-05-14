import sys
from collections import defaultdict

test_input = """
1
3 4
#.##
....
#.##
##
"""
test_lines = [line.strip() for line in test_input.strip().split("\n")]


def test_input() -> str:
    global test_lines
    res = test_lines[0]
    test_lines = test_lines[1:]
    return res


# =======================
output_test_id = 1


def err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    sys.stderr.flush()


def flush_print(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()


def case_print(s):
    global output_test_id
    flush_print("Case #{}: {}".format(output_test_id, s))
    output_test_id += 1


def receive_line() -> str:
    s = input()
    if s.strip() == "-1":
        sys.exit(0)
    return s.strip()


# ****************************
# myinput = input
myinput = test_input
# myinput = receive_line


cache = dict()
def f(b, x0, y0, w, h): # force win, force lose
    if w <= 0 or h <= 0:
        return 0, 1
    if (x0, y0, w, h) in cache:
        return cache[(x0, y0, w, h)]
    res = 0
    for x in range(x0, x0+w):
        if any((x,y) in b for y in range(y0, y0+h)):
            continue
        if f(b, x0, y0, x-x0, h) == 0 or f(b, x+1, y0, w-(x-x0)-1, h) == 0:
            res += h
    for y in range(y0, y0+h):
        if any((x,y) in b for x in range(x0, x0+w)):
            continue
        if f(b, x0, y0, w, y-y0) == 0 or f(b, x0, y+1, w, h-(y-y0)-1) == 0:
            res += h
    cache[(x0, y0, w, h)] = res
    return res


def solve_one_test_case():
    h,w = map(int, myinput().split())
    bb = [list(myinput()) for _ in range(h)]
    cc = set()
    for y in range(h):
        for x in range(w):
            if bb[y][x] == "#":
                cc.add((x,y))
    cache.clear()
    res = f(cc, 0, 0, w, h)
    case_print(res)


def mymain():
    t, = map(int, myinput().split())

    for _ in range(t):
        solve_one_test_case()


mymain()
