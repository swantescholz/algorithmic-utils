import itertools
import sys, re
from collections import defaultdict

from myutil import *
from LinkedList import LinkedList

alpha = "abcdefghijklmnopqrstuvwxyz"

lines = [it.strip() for it in open("../in.txt") if not it.isspace()]
coords = list()
for line in lines:
    x,y = map(int, line.split(", "))
    coords.append((x,y))
scoords = set(coords)
minx = min(x for (x,y) in coords)
miny = min(y for (x,y) in coords)
maxx = max(x for (x,y) in coords)
maxy = max(y for (x,y) in coords)
print(minx, miny, maxx, maxy)


def foo(x, y):
    doubled = False
    besti, bestd = -1, 10**22
    for i, (x0,y0) in enumerate(coords):
        d = abs(x0-x)+abs(y0-y)
        if d == bestd:
            doubled = True
        elif d < bestd:
            doubled = False
            besti = i
            bestd = d
    if doubled:
        return -1
    return besti

d = defaultdict(int)
for y in range(miny, maxy + 1):

    for x in range(minx, maxx + 1):
        i = foo(x,y)
        d[i] += 1

coords2i = dict((p,i) for i,p in enumerate(coords))
outer = set()
outer |= set((x,miny) for x in range(minx, maxx + 1))
outer |= set((x,maxy) for x in range(minx, maxx + 1))
outer |= set((minx,y) for y in range(miny, maxy + 1))
outer |= set((maxx,y) for y in range(miny, maxy + 1))
for p in outer:
    if p in scoords:
        d.pop(coords2i[p], None)
d.pop(-1, None)
print(max(d.values()))
