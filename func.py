# -*- coding: utf-8 -*-
"""
Allgemeinte Funktionen für matplotlib

@author: j.wagner
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable


PATH_IMG = r'export'

def save_fig(fig, name):
    fig.savefig(PATH_IMG+'/'+name, dpi=300, bbox_inches='tight')
    
    
    
    
    
### Ticks
 
def ticks_minor(ax, which='x', minorCount=2):
    if which=='x':
        xtick = ax.get_xticks()
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(np.diff(xtick)[0]/minorCount))
        return
    if which=='y':
        ytick = ax.get_yticks()
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(np.diff(ytick)[0]/minorCount))
        return
    if which=='both':
        ticks_minor(ax, 'x', minorCount)
        ticks_minor(ax, 'y', minorCount)
        return
    raise ValueError("keyword 'which' has to be 'x', 'y' or 'both'")
    
def ticks_other(ax, which='x'):
    if which=='x':
        ax.tick_params(direction='in', top=True, bottom=True, which='both')
        return
    if which=='y':
        ax.tick_params(direction='in', left=True, right=True, which='both')
        return
    if which=='both':
        ticks_other(ax, 'x')
        ticks_other(ax, 'y')
        return
    raise ValueError("keyword 'which' has to be 'x', 'y' or 'both'")
        
def ticks_handle(ax, which='x', other=True, minorCount=2):
    ax.tick_params(direction='in')
    ticks_minor(ax, which, minorCount)
    if other:
        ticks_other(ax, which)
        
   
    


### AXS
def ax_square(ax):
    ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='datalim')

  
# Helper function used for visualization in the following examples
def identify_axes(ax_dict=None, fontsize=48, p=False):
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
    
    if type(ax_dict) == np.ndarray:
        ax_dict = ax_dict.flatten()
        ax_dict = {(k): a for k, a in enumerate(ax_dict)}
    elif type(ax_dict) == tuple:
        ax_dict = list(ax_dict)
    elif ax_dict==None:
        fig = plt.gcf()
        ax_dict = list(fig.axes)
    if type(ax_dict) == list:
        ax_dict = {(k): a for k, a in enumerate(ax_dict)}
        
    if p:
        print('Type: ', type(ax_dict))
        print('Length:',len(ax_dict))
    kw = dict(ha="center", va="center", fontsize=fontsize, color="darkgrey")
    for k, ax in ax_dict.items():
        ax.text(0.5, 0.5, k, transform=ax.transAxes, **kw)
    return ax_dict

def next_color(ax):
    return next(ax._get_lines.prop_cycler)['color']
    
    
def axs_hide(axs, identify=False):
    if type(axs) == np.ndarray:
        axs = list(axs.flatten())
        # axs = list(axs)
    if type(axs) != list:
        axs = [axs]
    for ax in axs:
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)    
    if identify: identify_axes(axs)
    return axs






def add_colorbar(ax, im, **kwargs):    
    divider = make_axes_locatable(ax)
    ax_cb = divider.new_horizontal(size="5%", pad=0.05)
    fig = ax.get_figure()
    fig.add_axes(ax_cb)
    fig.colorbar(im, cax=ax_cb, **kwargs)

def color_axis(ax, color, xaxis:bool = True,yaxis:bool = False, other: bool = False):
    if xaxis:
        ax.xaxis.label.set_color(color)
        ax.tick_params(axis='x', colors=color)
        # label='bottom' if not other else 'top'
        # ax.spines[label].set_color(color)
    
    if yaxis:
        ax.yayis.label.set_color(color)
        ax.tick_params(axis='y', colors=color)
        # label='left' if not other else 'right'
        # ax.spines[label].set_color(color)
    




        