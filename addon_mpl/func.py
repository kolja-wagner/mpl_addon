# -*- coding: utf-8 -*-
"""
Ergänzende Funktionen zu matplotlib
@author: kolja
"""

import matplotlib.ticker as ticker
import numpy as np
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable

PATH_IMG = r'IMAGES'


def save_fig(fig, name):
    """ Export figure to file with standart settings."""
    if not os.path.exists(PATH_IMG):
        os.makedirs(PATH_IMG)
    fig.savefig(PATH_IMG + '/' + name, dpi=300, bbox_inches='tight')


def next_color(ax):
    return next(ax._get_lines.prop_cycler)['color']


def ticks_minor(ax, which: str = 'both', n: int = 2):
    """Set n minor ticks on axes for x, y or both axis."""
    if which == 'x' or which == 'both':
        xtick = ax.get_xticks()
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(np.diff(xtick)[0] / n))
    if which == 'y' or which == 'both':
        ytick = ax.get_yticks()
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(np.diff(ytick)[0] / n))
    if which not in ['x', 'y', 'both']:
        raise ValueError(f"keyword 'which' has to be 'x', 'y' or 'both' but is {which}")


def ticks_other(ax, which: str = 'both'):
    """Display both axis on axes for x, y or both."""
    if which == 'x' or which == 'both':
        ax.tick_params(direction='in', top=True, bottom=True, which='both')
    elif which == 'y' or which == 'both':
        ax.tick_params(direction='in', left=True, right=True, which='both')
    if which not in ['x', 'y', 'both']:
        raise ValueError(f"keyword 'which' has to be 'x', 'y' or 'both' but is {which}")


def ticks_handle(ax, which: str = 'both', other: bool = True, n: int = 2):
    """Combine ticks_minor and ticks_other. """
    ax.tick_params(direction='in')
    ticks_minor(ax, which, n)
    if other:
        ticks_other(ax, which)


def ax_square(ax):
    """ Set box aspect of axes to 1."""
    ax.set_box_aspect(1.0)


def ax_hide(ax, which: str = 'both'):
    """ Hide the spine of x, y or both axis."""
    if which == 'x' or which == 'both':
        ax.axes.xaxis.set_visible(False)
    if which == 'y' or which == 'both':
        ax.axes.yaxis.set_visible(False)
    if which not in ['x', 'y', 'both']:
        raise ValueError(f"keyword 'which' has to be 'x', 'y' or 'both' but is {which}")


def ax_color(ax, color, which: str = 'x', all: bool = False,  other: bool = False):
    if which == 'x' or which == 'both':
        ax.xaxis.label.set_color(color)
        ax.tick_params(axis='x', colors=color)
        if all:
            label = 'bottom' if not other else 'top'
            ax.spines[label].set_color(color)
    if which == 'y' or which == 'both':
        ax.yayis.label.set_color(color)
        ax.tick_params(axis='y', colors=color)
        if all:
            label = 'left' if not other else 'right'
            ax.spines[label].set_color(color)
    if which not in ['x', 'y', 'both']:
        raise ValueError(f"keyword 'which' has to be 'x', 'y' or 'both' but is {which}")


# Helper function used for visualization in the following examples
def identify_axes(ax_dict=None, fontsize=48):
    """  Helper to identify the Axes in the examples below.
    Parameters
    ----------
    ax_dict : dict[str, Axes]
        Mapping between the title / label and the Axes.
    fontsize : int, optional
        How big the label should be.
    p : bool, optional
        Print some stats
    """
    kw = dict(ha="center", va="center", fontsize=fontsize, color="darkgrey")
    for k, ax in ax_dict.items():
        ax.text(0.5, 0.5, k, transform=ax.transAxes, **kw)
    return ax_dict


def add_colorbar(ax, im, **kwargs):
    divider = make_axes_locatable(ax)
    ax_cb = divider.new_horizontal(size="5%", pad=0.05)
    fig = ax.get_figure()
    fig.add_axes(ax_cb)
    fig.colorbar(im, cax=ax_cb, **kwargs)
