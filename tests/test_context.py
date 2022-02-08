# -*- coding: utf-8 -*-
"""
Test PlotRowobject
@author: j.wagner
"""

import addon_mpl.context as pM


def basic_test():
    with pM.Figure('Figure with add_subplot', save=True) as im:
        ax = im.add_ax(im.fig.add_subplot())
        ax.plot([1,2],[1,2])
        assert im.axs[0] == ax
        assert im.fig.get_axes()[0] == ax
        print(f"test '{im.name}' sucessfull")
    
    with pM.PlotGrid('PlotGrid without split',n=3, m=2, split=False, save=True) as im:
        assert im.fig.get_axes()[0] == im.axs[0]
        assert im.fig.get_axes()[2] == im.axs[2]
        print(f"test '{im.name}' sucessfull")

    with pM.PlotRow('PlotRow without split', n=3, split=False, save=True) as im:
        axes = im.fig.get_axes()
        for i, ax in enumerate(axes):
            assert im.axs[i] == ax
        print(f"test '{im.name}' sucessfull")

    with pM.PlotStack('PlotStack without split',n=3, split=False, save=True) as im:
        axes = im.fig.get_axes()
        for i, ax in enumerate(axes):
            assert im.axs[i] == ax
        print(f"test '{im.name}' sucessfull")

    with pM.PlotGrid('PlotGrid with split',n=3, m=2,
                     split=True, save=True) as im:
        for fig, ax in zip(im.figs, im.axs):
            assert ax in fig.get_axes()
        print(f"test '{im.name}' sucessfull")


def main():

    basic_test()
    
    pass

if __name__=='__main__':
    main()