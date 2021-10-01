# -*- coding: utf-8 -*-
"""
Test PlotRowobject
@author: j.wagner
"""

import context as pM


def basic_test():
    with pM.Figure('Figure with add_subplot', saveFigure=False) as im:
        ax = im._add_subplot()
        ax.plot([1,2],[1,2])
        
        assert im.ax0 == ax
        assert im.axs[0] == ax
        assert im.fig.get_axes()[0] == ax
        print(im)
        print('test sucessfull')
    
    # with pM.PlotGrid('PlotGrid without split',n=3, m=2, folder = 'arbeitspunkt',split=False, saveFigure=False) as im:
    #     assert im.fig.get_axes()[0] == im.axs[0]
    #     assert im.axs[0] == im.ax0
    #     assert im.fig.get_axes()[2] == im.axs[2]
    #     assert im.axs[2] == im.ax2
    #     print(im)
    #     print('test sucessfull')
            
    # with pM.PlotRow('Plotrow without split',n=3, folder = 'arbeitspunkt',split=False, saveFigure=False) as im:
    #     axes = im.fig.get_axes()
    #     for i, ax in enumerate(axes):
    #         assert im.axs[i] == ax
    #     assert im.axs[0] == im.ax0
    #     assert im.axs[2] == im.ax2
    #     print(im)
    #     print('test sucessfull')
    
    # with pM.PlotStack('Plotrow without split',n=3, folder = 'arbeitspunkt',split=False, saveFigure=False) as im:
    #     axes = im.fig.get_axes()
    #     for i, ax in enumerate(axes):
    #         assert im.axs[i] == ax
    #     assert im.axs[0] == im.ax0
    #     assert im.axs[2] == im.ax2
    #     print(im)
    #     print('test sucessfull')
        
        
    # with pM.PlotGrid('PlotGrid with split',n=3, m=2,
    #                  split=True, saveFigure=True) as im:
    #     for fig, ax in zip(im.figs, im.axs):
    #         assert ax in fig.get_axes()
    #     assert im.ax0 in im.fig0.get_axes()
    #     assert im.ax5 in im.fig5.get_axes()
    #     print(im)
    #     print('test sucessfull')
# basic_test()

def main():

    basic_test()
    
    pass

if __name__=='__main__':
    main()