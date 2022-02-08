# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:54:56 2021

@author: Harin
"""

import addon_mpl.func as pM
# import addon_mpl.context as pC


import matplotlib.pyplot as plt
import numpy as np

pM.PATH_IMG = '../IMAGES'


fig,axs = plt.subplots(3,3)


x = np.linspace(0,5,100)
y = np.cos(x)

for i in range(3):
    for j in range(3):
        axs[i][j].plot(x**(i+1),y**(j+1))
        pM.ax_square(axs[i][j])

    pM.ax_color(axs[i][0], 'red')
    pM.ax_color(axs[i][1], 'red', all=True)
    pM.ax_color(axs[i][2], 'red', all=True, other=True)


plt.show()


pM.save_fig(plt.gcf(), 'test')
#
# with pC.Figure('test', showTitle=True) as im:
#     im.ax=im.fig.add_subplot()
#
#     im.ax.plot(x,y)
#
# with pC.Plot('test2', showTitle=True, square=True) as im:
#     im.ax.plot(x,-y)
#     print(im.square)
#
# with pC.PlotGrid('test3', n=2,m=1, showTitle=True, saveFigure=False,
#                  square=True, split=False) as im:
#     ax1, ax2 = im.axs[0], im.axs[1]
#     ax1.plot(x,y)
#     ax2.plot(y,x)
#
# # fig, ax = plt.subplots(2,2, subplot_kw={'box_aspect':1})
#
# # ax.set_box_aspect(1)
# # bx= ax.twinx()
# # ax.set_box_aspect(1)
#

# pM.ax_square(ax)
# pM.ticks_handle(ax, 'both')

# ax.set_aspect(1.0/ax.get_data_ratio())
