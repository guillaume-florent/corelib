#!/usr/bin/env python
# coding: utf-8

r"""Bspline demo"""

import matplotlib.pyplot as plt
import numpy as np

from corelib.geometry.bspline import bspline

colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')

cv = np.array([[50., 25.],
               [59., 12.],
               [50., 10.],
               [57.,  2.],
               [40.,  4.],
               [40., 14.]])

plt.plot(cv[:, 0], cv[:, 1], 'o-', label='Control Points')

for d in range(1, 21):
    p = bspline(cv, n=200, degree=d, periodic=False)
    x, y = p.T
    plt.plot(x, y, 'k-', label='Degree %s' % d, color=colors[d % len(colors)])

plt.minorticks_on()
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(35, 70)
plt.ylim(0, 30)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
