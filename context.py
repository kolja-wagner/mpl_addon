# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:48:37 2021

@author: Harin
"""

import matplotlib.pyplot as plt
import os

import numpy as np


from func import save_fig

# FIGURE AND SUBCLASSES
class Figure(object):
    ''' Context Manager für matplotlib. Automatisches Speichern.'''
    def __init__(self, 
                 name:          str,        # Filename and possible title
                 subfolder:     str = None, # Subolder for saving
                 baselength:    int = 5,    # Lenght of axes (inches)
                 square:        bool=False, # make axes square
                 showTitle:     bool=False, # Show name as title
                 saveFigure:    bool=False  # Save Figure(s)
                 ):
        
        self.name=name
        self.baselength= baselength
        self.saveFigure = saveFigure
        self.square = square
        
        self.folder='' if subfolder == None else subfolder
        self.showName = False if self.saveFigure else showTitle
    
        self.figs = []                      # save all figures
        self.axs =  []                      # and all axes

    @property
    def names(self):
        if len(self.figs) <=1: return [self.name]
        return [f'{self.name}_{chr(i+97)}' for i in range(len(self.figs))]
        
    def fig_save(self):
        for i, fig in enumerate(self.figs):
            path = os.path.join(self.folder,self.names[i])
            save_fig(fig, path)
    
    def fig_title(self):
        for fig, name in zip(self.figs, self.names):
            fig.suptitle(name)
                
    def set_baselength(self, l: float):
        if len(self.figs) == 0:
            return
        for f in self.figs:
            f.set_figheight(l)
            f.set_figwidth(l)
        
    def add_fig(self, fig: plt.Figure) -> plt.Figure:
        # setattr(self, f'fig{len(self.figs)-1}', self.fig)
        self.figs.append(fig)
        return fig
    
    def add_ax(self, ax: plt.Axes) -> plt.Axes:
        if self.square:
            ax.set_box_aspect(1)
        self.axs.append(ax)
        
    def __enter__(self):
        self.fig= plt.figure(figsize=(self.baselength, self.baselength))
        self.figs.append(self.fig)
        return self
        
    def __exit__(self, type, value, traceback):
        if self.showName:
            self.fig_title()
        if not self.saveFigure:
            return
        for f, n in zip(self.figs, self.names):
            save_fig(f,n)
            
           
class Plot(Figure):
    def __enter__(self):
        self.fig, self.ax = plt.subplots(figsize=(self.baselength, self.baselength))
        self.add_fig(self.fig)
        self.add_ax(self.ax)
        return self
    
class PlotGrid(Plot):
    def __init__(self, name: str, 
                 n: int=1, m: int=1, 
                 *args, **kwargs):
        self.n = n
        self.m = m
        self.split = kwargs.pop('split',False)
        self.gridspec = kwargs.pop('gridspec_kw', None)
        super().__init__(name, *args, **kwargs)
        
    def __enter__(self):
        if self.n == 1 and self.m==1:
            super().__enter__()
            return self
        
        if self.split:
            for n in range(self.n*self.m):
                fig = plt.figure(figsize=(self.baselength, self.baselength))
                ax = fig.add_subplot()
                self.add_fig(fig)
                self.add_ax(ax)
                
        if not self.split:
            self.fig, self.axs = plt.subplots(self.m, self.n,constrained_layout=True, 
                                              figsize=(self.n*self.baselength,self.m*self.baselength),
                                              gridspec_kw=self.gridspec)
            self.figs = [self.fig]
            self.axs = self.axs.flatten()
            
        return self
    
    def set_baselength(self, l):
        if self.split:
            super().set_baselength(l)
            return
        self.fig.set_figheight(l*self.m)
        self.fig.set_figwidth(l*self.n)
                  
class PlotRow(PlotGrid):
    def __init__(self, name:str,
                  n: int,
                  *args, **kwargs):
        super().__init__(name=name, n=n, m=1, *args, **kwargs)

class PlotStack(PlotGrid):
    def __init__(self, name:str,
                  n: int,
                  *args, **kwargs):
        super().__init__(name=name, n=1, m=n, *args, **kwargs)

        