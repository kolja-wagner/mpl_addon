# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:54:56 2021

@author: Harin
"""


import matplotlib.pyplot as plt
import numpy as np
import addon_mpl.func as pM

pM.PATH_IMG = '../IMAGES'


def test_func_square():
    x = np.linspace(0, 5, 100)
    y = np.cos(x)
    plt.plot(x,y)
    plt.title('SQUARE')
    pM.ax_square(plt.gca())
    pM.save_fig(plt.gcf(), 'test_square')
    plt.show()

def test_func_ticks():

    x = np.linspace(0,5,100)
    y = np.cos(x)

    fig, (ax, bx, cx) = plt.subplots(1,3, figsize=(6,3), tight_layout=True)
    for xx in [ax,bx,cx]:
        xx.plot(x,y)
    ax.set_title('minor: x=4')
    pM.ticks_minor(ax, which='x', n=4)
    bx.set_title('other: y')
    pM.ticks_other(bx, which='y')
    cx.set_title('handle: both')
    pM.ticks_handle(cx, which='both')
    fig.suptitle('TICKS')

    pM.save_fig(fig, 'test_ticks')
    plt.show()


def test_func_misc():
    x = np.linspace(0,5,100)
    y = np.cos(x)

    fig, (ax, bx, cx) = plt.subplots(1,3, figsize=(6,3), tight_layout=True)

    ax.set_title('next_color')
    pM.next_color(ax)
    for xx in [ax,bx,cx]:
        xx.plot(x,y)
    bx.set_title('ax_color')
    pM.ax_color(bx, 'blue', all=True)
    cx.set_title('ax_hide')
    pM.ax_hide(cx, which='both')
    pM.save_fig(fig, 'test_misc')
    plt.show()


def test_identify_ax():
    fig = plt.figure(figsize=(6, 3), constrained_layout=True)
    # for details see https://matplotlib.org/stable/tutorials/provisional/mosaic.html
    axd = fig.subplot_mosaic(
        """
        AB
        AC
        """
    )
    pM.identify_axes(axd)
    axd['A'].plot([0, 1], [1, 2])
    plt.show()

    fig, axs = plt.subplots(3, 2)
    pM.identify_axes(axs)
    plt.show()

def main():

    test_func_square()
    test_func_ticks()
    test_func_misc()
    test_identify_ax()


if __name__ == '__main__':
    main()


