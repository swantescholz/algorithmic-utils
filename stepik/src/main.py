import random

res_path = "/home/swante/downloads/"
test_lines = [line.strip() for line in open(res_path + "input.txt")]
random.seed(1)


def input():
    global test_lines
    res = test_lines[0]
    test_lines = test_lines[1:]
    return res


# =======================
import sys, math, fractions

possible, impossible = "POSSIBLE", "IMPOSSIBLE"
output_test_id = 1
out_file = open(res_path + "output.txt", "w")

def case_print(s):
    global output_test_id
    # print("Case #{}: {}".format(output_test_id, s))
    out_file.write(f"{s}\n")
    print(s)
    output_test_id += 1


def print_flush(s):
    print(s)
    sys.stdout.flush()


# ****************************

def solve_one_test_case():
    a,b = map(int, input().split())
    return a+b


def mymain():
    t = int(input())
    for _ in range(t):
        case_print(solve_one_test_case())


mymain()
