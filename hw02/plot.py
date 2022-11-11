#!/usr/bin/bash
from cProfile import label
import matplotlib.pyplot as plt
import seaborn
import numpy as np
seaborn.set_style("whitegrid")
plt.rcParams.update({'font.size': 16})

fig, ax = plt.subplots(figsize=[8,6])
ax.set_ylim([-0.1, 1.3])
x1 = [
    [-3/2, 0],
    [-1, 1/2],
    [1, 1/2],
    [3/2, 0]
]
x2 = [
    [-2, 0],
    [0, 1],
    [2, 0],
]
x3 = [
    [-5/2, 0],
    [-1/2, 1],
    [1/2, 1],
    [5/2, 0]
]
x4 = [
    [-3, 0],
    [-1, 1],
    [1, 1],
    [3, 0]
]
x5 = [
    [-6, 0],
    [-4, 1],
    [4, 1],
    [6, 0]
]
ax.plot(np.array(x1)[:, 0], np.array(x1)[:, 1], label=r"$t=a/2c$")
ax.plot(np.array(x2)[:, 0], np.array(x2)[:, 1], label=r"$t=a/c$")
ax.plot(np.array(x3)[:, 0], np.array(x3)[:, 1], label=r"$t=3a/2c$")
ax.plot(np.array(x4)[:, 0], np.array(x4)[:, 1], label=r"$t=2a/c$")
ax.plot(np.array(x5)[:, 0], np.array(x5)[:, 1], label=r"$t=5a/c$")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$u$")

fig.canvas.draw()

ylabels = [w.get_text()+r" $a/c$" for w in ax.get_yticklabels()]
print(ylabels)
ylabels = ax.set_yticklabels(ylabels)

plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig("q2.pgf")
# plt.show()

