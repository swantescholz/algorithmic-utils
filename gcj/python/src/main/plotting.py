"""3d function(x,y) -> z surface grid plotting
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

import numpy as np

def fun(x, y):
	p = 14
	return (np.abs(x)**p + np.abs(y)**p)**(1.0/p)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-3.0, 3.0, 0.04)
X, Y = np.meshgrid(x, y)
zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
plt.show()
"""
import matplotlib

"""scatterplot
import numpy as np
import matplotlib.pyplot as plt


m = np.loadtxt("/home/swante/Dropbox/uef/clu/ex1/foo.txt")
plt.scatter(m[:,0],m[:,1])
plt.show()

"""

"""simple plot

t = np.linspace(0,8,1000)
plt.plot(t,np.sin(t))
plt.show()
"""

"""with legend, axis labels

"""

matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt


def quit_figure(event):
	if event.key == 'escape':
		plt.close(event.canvas.figure)


def myshow(block=True):
	plt.gcf().canvas.mpl_connect('key_press_event', quit_figure)
	plt.show(block=block)


if __name__ == "__main__":
	t = np.linspace(0, 1, 100)
	import math
	def log2(x):
		if x == 0:
			return 0
		return math.log2(x)
	y = [-x*log2(x)-(1-x)*log2(1-x) for x in t]
	plt.plot(t,y,"b-")
	plt.xlabel("p_head")
	plt.ylabel("H(X_p)")
	myshow()
