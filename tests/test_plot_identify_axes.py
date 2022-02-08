# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 14:17:09 2021

@author: j.wagner
"""

import matplotlib.pyplot as plt
import plot.master as pM

def test_identify_axes():
    
    fig, axs = plt.subplots(3,2)
    pM.identify_axes(axs) 
    
    fig = plt.figure(figsize=(12,6),constrained_layout=True)
    # for details see https://matplotlib.org/stable/tutorials/provisional/mosaic.html
    axd = fig.subplot_mosaic(
        """
        AB
        AC
        """
    )
    pM.identify_axes(axd)
    axd['A'].plot([0,1],[1,2])
    pM.standartoptions(axd['A'])
    
    print(type(axd)==dict)
    
    
def main():
    test_identify_axes()

if __name__=='__main__':
    main()