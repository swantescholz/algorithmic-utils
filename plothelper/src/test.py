import matplotlib

# matplotlib.use("TkAgg")
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt

def quit_figure(event):
    if event.key == 'escape':
        plt.close(event.canvas.figure)

def myshow(block=True):
    plt.gcf().canvas.mpl_connect('key_press_event', quit_figure)
    plt.show(block=block)


t = np.linspace(1.0, 25.0, 50)
x = np.cos(t)*t
y = np.sin(t)*t
plt.plot(x,y, "bs-")
myshow()