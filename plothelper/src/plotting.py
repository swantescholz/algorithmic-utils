import sys
from typing import List

import matplotlib
import pandas as pd

matplotlib.use("TkAgg")
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.float_format', lambda x: "{:.6g}".format(x))
matplotlib.rcParams.update({'font.size': 24})
def make_data_frame(data: np.ndarray, columns_labels=None, row_labels=None):
    return pd.DataFrame(data=data, columns=columns_labels, index=row_labels)

def get_my_line_styles() -> List[str]:
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    dot_styles = ["-", "--", "-.", ":", "-", "--", "-."]
    marker_styles = ["o", "s", "^", "P", "D", "v", "X"]
    return [colors[i] + marker_styles[i] + dot_styles[i] for i in range(len(colors))]

def get_default_color_list():
    res = ["red", "blue", "green", "orange", "purple", "brown", "yellow"]
    for cname in matplotlib.colors.cnames.keys():
        if cname not in res:
            res.append(cname)
    return res

def quit_figure(event):
    if event.key == 'escape':
        plt.close(event.canvas.figure)

def save_image(path: str, width_px: int, height_px: int):
    fig = matplotlib.pyplot.gcf()
    dpi = fig.get_dpi()
    fig.set_size_inches(width_px/dpi, height_px/dpi)
    fig.savefig(path, dpi=dpi)#, bbox_inches='tight', pad_inches=0)

def myshow(block=True):
    plt.gcf().canvas.mpl_connect('key_press_event', quit_figure)
    plt.tight_layout(0.0)
    plt.show(block=block)


def plot_colored_grid(xymin, xymax, get_labels_for_xys_function, grid_size=100, color_list=None):
    """
    for (x,y) pairs evenly spaced in a grid, determine their class labels, and then plot
    squares with different colors accordingly, so that the decision regions for classification can
    be visualized
    alternative? : plt.imshow(data_ints, extent=[0, 1, 0, 1])
    """
    if color_list is None:
        color_list = get_default_color_list()

    xs = np.linspace(xymin[0],xymax[0], grid_size)
    ys = np.linspace(xymin[1], xymax[1], grid_size)
    xys = np.zeros((grid_size**2,2))
    for y in range(len(ys)):
        for x in range(len(xs)):
            xys[y*grid_size+x,0] = xs[x]
            xys[y * grid_size + x,1] = ys[y]
    labels = get_labels_for_xys_function(xys)
    labels = np.array(labels).astype(np.int).reshape((grid_size,grid_size))
    labels = np.flip(labels, axis=0)
    color_list = color_list[:np.max(labels)+1]
    cmap = colors.ListedColormap(color_list)
    plt.imshow(labels, cmap=cmap, interpolation='none', extent=(xymin[0], xymax[0], xymin[1], xymax[1]))



def test_grid():
    def f(xys):
        # return np.random.randint(0,8,size=(len(xys),1))
        return xys[:,0]**2 < xys[:,1]
    plot_colored_grid((-10,-10), (10,15), f, grid_size=222)
    myshow()

if __name__ == '__main__':
    test_grid()
    sys.exit()
    ts = np.linspace(0,10,50)
    xs = np.cos(ts) * ts
    ys = np.sin(ts) * ts
    plt.plot(ts,xs)
    plt.scatter(xs,ys)
    myshow()