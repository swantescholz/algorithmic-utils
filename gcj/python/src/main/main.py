import sys
from collections import defaultdict

test_input = """
3
1
RS
3
R
P
S
7
RS
RS
RS
RS
RS
RS
RS
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
myinput = input
# myinput = test_input
# myinput = receive_line

def fight(a,b):
    if a == b:
        return 0
    if a == "R" and b == "P":
        return 1
    if a == "R" and b == "S":
        return -1
    if a == "P" and b == "R":
        return -1
    if a == "P" and b == "S":
        return 1
    if a == "S" and b == "R":
        return 1
    return -1

def solve_one_test_case():
    a, = map(int, myinput().split())
    cc = []
    wins_against = {"R": "P", "P": "S", "S": "R"}
    for i in range(a):
        cc.append((myinput()*500)[:500])
    s = set(cc)
    res = ""
    for i in range(500):
        if len(s) == 0:
            case_print(res)
            return
        t = set(e[i] for e in s)
        if len(t) == 3:
            case_print("IMPOSSIBLE")
            return
        if len(t) == 1:
            res += wins_against[t.pop()]
            case_print(res)
            return
        x = "S"
        if t == {"R","S"}:
            x = "R"
        if t == {"R","P"}:
            x = "P"
        res += x
        s = set(it for it in s if it[i] == x)
    case_print("IMPOSSIBLE")




def mymain():
    t, = map(int, myinput().split())

    for _ in range(t):
        solve_one_test_case()


mymain()
