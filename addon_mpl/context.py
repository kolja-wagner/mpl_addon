# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:48:37 2021

@author: Kolja
"""
import matplotlib.pyplot as plt

import addon_mpl.func as func


class Figure:
    def __init__(self,
                 name: str,
                 size: int = 4,
                 show: bool = True,
                 save: bool = False,
                 path: str = None):
        self.name = name
        self.basesize = size
        self.show = show
        self.save = save
        self.folder = func.PATH_IMG if path is None else path

        self.figs = list()
        self.axs = list()

    @property
    def names(self):
        if len(self.figs) <= 1:
            return [self.name]
        return [f'{self.name}_{chr(i+97)}' for i,_ in enumerate(self.figs)]

    def __enter__(self):
        fig = plt.figure(figsize=(self.basesize, self.basesize))
        self.fig = fig
        self.figs.append(fig)
        return self

    def __exit__(self, typ, value, traceback):
        if self.show:
            plt.show()
        if not self.save:
            return
        for f, n in zip(self.figs, self.names):
            print(f"Figure '{n}' saved at '{self.folder}'.")
            func.save_fig(f, n, path=self.folder)

    def add_fig(self, fig: plt.Figure) -> plt.Figure:
        self.figs.append(fig)
        return fig

    def add_ax(self, ax: plt.Axes) -> plt.Axes:
        self.axs.append(ax)
        return ax

    def set_basesize(self, size: float):
        if len(self.figs) == 0:
            return
        for f in self.figs:
            f.set_figheight(size)
            f.set_figwidth(size)


class Plot(Figure):
    def __enter__(self):
        self.fig, self.ax = plt.subplots(figsize=(self.basesize, self.basesize))
        self.add_fig(self.fig)
        self.add_ax(self.ax)
        return self


class PlotGrid(Plot):
    def __init__(self, name: str, n: int = 1, m: int = 1, *args, **kwargs):
        self.n = n
        self.m = m
        self.split = kwargs.pop('split', False)
        self.gridspec = kwargs.pop('gridspec_kw', None)
        super().__init__(name, *args, **kwargs)

    def __enter__(self):
        if self.n == 1 and self.m == 1:
            super().__enter__()
            return self

        if self.split:
            for n in range(self.n * self.m):
                fig = plt.figure(figsize=(self.basesize, self.basesize))
                ax = fig.add_subplot()
                self.add_fig(fig)
                self.add_ax(ax)

        if not self.split:
            self.fig, self.axs = plt.subplots(self.m, self.n, constrained_layout=True,
                                              figsize=(self.n * self.basesize, self.m * self.basesize),
                                              gridspec_kw=self.gridspec)
            self.figs = [self.fig]
            self.axs = self.axs.flatten()
            self.ax = self.axs[0]

        return self

    def __exit__(self, *args):
        super().__exit__(*args)

    def set_basesize(self, size: float):
        if self.split:
            super().set_basesize(size)
            return
        self.fig.set_figheight(size * self.m)
        self.fig.set_figwidth(size * self.n)


class PlotRow(PlotGrid):
    def __init__(self, name: str, n: int, *args, **kwargs):
        super().__init__(name=name, n=n, m=1, *args, **kwargs)


class PlotStack(PlotGrid):
    def __init__(self, name: str, n: int, *args, **kwargs):
        super().__init__(name=name, n=1, m=n, *args, **kwargs)
