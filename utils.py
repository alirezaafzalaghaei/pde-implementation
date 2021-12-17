import numpy as np
import matplotlib
import seaborn as sns
from tabulate import tabulate
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_heatmap(u, t, sampling):

    samples_u = u[::sampling]
    samples_t = t[::sampling]
    fig, (axes) = plt.subplots(figsize=(8, 3))
    vmin, vmax = u.min(), u.max()
    legend_t = list(map(lambda t: 't = %0.3f' % t, samples_t))

    def init():
        axes.set_title(legend_t[0])
        sns.heatmap(np.zeros_like(samples_u[[0]]),
                    vmin=vmin,
                    vmax=vmax,
                    ax=axes,
                    cbar=False)

    def animate(i):
        axes.set_title(legend_t[i])
        sns.heatmap(samples_u[[i]], vmin=vmin, vmax=vmax, ax=axes, cbar=False)

    anim = FuncAnimation(fig,
                         animate,
                         init_func=init,
                         frames=len(samples_u),
                         interval=1,
                         repeat=False)
    return anim


def animate_line(u, t, sampling=200):

    samples_u = u[::sampling]
    samples_t = t[::sampling]
    fig, (axes) = plt.subplots()

    legend_t = list(map(lambda t: 't = %0.3f' % t, samples_t))

    def init():
        axes.set_title(legend_t[0])
        axes.set_ylim(0, 1)
        return axes.plot(np.zeros_like(samples_u[[0]]).T, color='k')

    def animate(i):
        axes.clear()
        axes.set_ylim(0, 1)
        axes.set_title(legend_t[i])
        return axes.plot(samples_u[i].T, color='k')

    anim = FuncAnimation(fig,
                         animate,
                         init_func=init,
                         frames=len(samples_u),
                         interval=30,
                         repeat=False)
    return anim


def print_table(u, x, t=None, digits=4):
    tabulate_params = dict(tablefmt='fancy_grid',
                           headers="firstrow",
                           numalign='center',
                           stralign='center')

    Nt, Nx = u.shape
    R = np.empty((Nt + 2, Nx + 1), dtype=object)
    R[0, 0] = 'x'
    R[0, 1:] = x.round(digits)
    R[-1, 0] = 'x'
    R[-1, 1:] = x.round(digits)

    R[1:-1, 1:] = np.array(u).round(digits)
    for j in range(len(u)):
        if t is not None:
            R[1 + j, 0] = 'j=%d(t=%g)' % (j, t[j])
        else:
            R[1 + j, 0] = 'j=%d' % j
    print(tabulate(R, **tabulate_params))