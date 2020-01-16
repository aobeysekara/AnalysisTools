#!/usr/bin/env python

###############################################################################
# Author: Dr. Asiri I.B. Obeysekara
# Date: 20/08/2019
#
#  {WORK IN PROGRESS}
#
#
###############################################################################

__author__="Asiri I.B. Obeysekara"
__copyright__ = "Copyright 2019, AnalysisTools - AObeysekara"
__credits__ = ["AMCG", "Imperial College London"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "A Obeysekara"
__email__ = "a.obeysekara@imperial.ac.uk"
__status__ = "Production"

import numpy as np
import matplotlib.pyplot as plt

class Plot():
    def __init__(self, file, label):
        self.file=file
        self.label=label

    def plotscatter(self,size,width,color,marker):
        x, y = np.loadtxt(self.file, delimiter=',', unpack=True)
        plt.plot(x,y, marker=marker,linestyle=' ', markersize=size,  markeredgecolor=color, fillstyle='none' , markeredgewidth=width, label=self.label)


    def plotline(self,size,width,color,style,msize):
        x, y = np.loadtxt(self.file, delimiter=',', unpack=True)
        plt.plot(x,y,label=self.label,color=color, linestyle=style, linewidth=width, markersize=msize)

if __name__ == '__main__':
    print('this is a csv module')
