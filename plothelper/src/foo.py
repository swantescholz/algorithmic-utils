import itertools
import math
import random
from collections import defaultdict
from pprint import pprint


def main():
    c = 3
    n = c*2-1
    base = list(range(n))
    for i, subset in enumerate(itertools.combinations(base, c)):
        idx = sum(subset) % c
        magic = subset[idx]


if __name__ == '__main__':
    main()
