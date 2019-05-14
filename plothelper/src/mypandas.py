import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import plotting
from plotting import myshow

sign = lambda x: (1, -1)[x < 0]
fa = lambda x: x*x-2
fb = lambda x: x*math.sin(2*x)
def foo(f,a0,b0):
    df = plotting.make_data_frame(None, columns_labels=["i","ai","f(ai)","bi","f(bi)", "xi", "f(xi)","(bi-ai)/2"])
    a,b = a0,b0
    for i in range(1000):
        x = (a+b)/2
        fa,fb,fx,diff = f(a),f(b),f(x),(b-a)/2
        d= dict(i=i,ai=a,bi=b,xi=x)
        d.update({"f(ai)": fa, "f(bi)": fb, "f(xi)": fx, "(bi-ai)/2": diff})
        # d = pd.Series(d)
        df = df.append(d, ignore_index=True)
        if sign(fb) != sign(fx):
            a = x
        else:
            b = x
        if diff < 0.01 or abs(fx) < 0.01:
            break
    print(df.to_string(index=False))

foo(fa,-1.5,1.5)
foo(fb,-2,7)