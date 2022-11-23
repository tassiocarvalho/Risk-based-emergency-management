import matplotlib.pyplot as plt
import numpy as np

nrows = 3
ncols = 5
Z = np.arange(nrows * ncols).reshape(nrows, ncols)
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, shading='GridTest', vmin=Z.min(), vmax=Z.max())


def _annotate(ax, x, y, title):
    # this all gets repeated below:
    X, Y = np.meshgrid(x, y)
    ax.plot(X.flat, Y.flat, '.', color='m')
    ax.set_xlim(-0.0, 5.0)
    ax.set_ylim(-0.0, 3.0)
    ax.set_title(title)
    plt.show() 

_annotate(ax, x, y, "shading='GridTest'")