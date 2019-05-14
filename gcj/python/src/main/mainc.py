import sys
from collections import defaultdict

test_input = """
5
3 3
...
...
...
1 1
.
1 2
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

def g(c, h, w, dx, dy, x, y):
    res = [(y,x)]
    for f in [-1, 1]:
        for i in range(1,max(h, w)):
            y2, x2 = y + f * i * dy, x + f * i * dx
            if x2 < 0 or y2 < 0 or x2 >= w or y2 >= h:
                break
            cc = c[y2][x2]
            if cc == "#":
                return None
            if cc == "x":
                break
            res.append((y2,x2))
    return res

def f(b, h, w):
    res = 0
    for y in range(h):
        for x in range(w):
            if b[y][x] != ".":
                continue
            for dx, dy in [(0,1),(1,0)]:
                r = g(b,h,w,dx,dy, x,y)
                if r is not None:
                    # c = [list(it) for it in b]
                    for (yy,xx) in r:
                        b[yy][xx] = "x"
                    if f(b,h,w) == 0:
                        res += 1
                    for (yy,xx) in r:
                        b[yy][xx] = "."

    return res


def solve_one_test_case():
    h,w = map(int, myinput().split())
    bb = [list(myinput()) for _ in range(h)]
    res = f(bb, h, w)
    case_print(res)


def mymain():
    t, = map(int, myinput().split())

    for _ in range(t):
        solve_one_test_case()


mymain()
