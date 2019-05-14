from collections import defaultdict
from typing import Callable

import matplotlib
import numpy as np
import sys

from d3.rectangle import rectangle
from d3.vec2 import vec2

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import queue, random, time, plotting
from d3.ipair import ipair
from ints import primes
import math
import os

counts = defaultdict(int)
for line in open("../../../../../downloads/worm.txt"):
	for word in line.split():
		word = word.lower()
		counts[word] += 1
print("done")
counts = [(v,k) for k,v in counts.items()]
counts.sort(reverse=True)
counts = [(k,v) for v,k in counts]
for i in range(5000):
	print(counts[i][0], counts[i][1])
print(len(counts))