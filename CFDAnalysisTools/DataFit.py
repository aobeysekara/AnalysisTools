#!/usr/bin/env python

###############################################################################
# Author: Dr. Asiri I.B. Obeysekara
# Date: 20/08/2019
#
#  {WORK IN PROGRESS}
#
# this pythong module allows the user to define a line to plot field variables
# from VTU and PVTU (parallel) files, which are the usual output files from
# CFD software IC-FERST
#
# classes: Filter class and plotting class.
#
#
# Filter class: inputs are path, filename and field for initilisation
#               line filter: inputs are the coordinates (in cartesian) of the
#               line
#
# Plotting class: inputs are X and Y fields
#                 returns a line in plt.
###############################################################################

__author__="Asiri I.B. Obeysekara"
__copyright__ = "Copyright 2019, AnalysisTools - AObeysekara"
__credits__ = ["AMCG", "Imperial College London"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "A Obeysekara"
__email__ = "a.obeysekara@imperial.ac.uk"
__status__ = "Production"

import matplotlib.pyplot as plt
import numpy as np
import vtk
from math import *
from scipy import interpolate
from scipy.signal import argrelextrema
from scipy.signal import find_peaks, peak_widths

class DataAnalysis():
    def __init__(self, X, Y, label, color,flag):
        self.X = X #
        self.Y = Y #currently a vector array
        self.label=label
        self.color=color
        self.flag=flag

    def VTKCurveFit(self, npol):
        from scipy.optimize import least_squares

        scaleX=[]
        scaleY=[]
        for i in range(len(self.X)-1):
            scaleX.append((self.X[i]-min(self.X))/max(self.X))
            scaleY.append((self.Y[i]-min(self.Y))/max(self.Y))

        #original data
        if self.flag=='T':
            plt.plot(scaleY,scaleX, marker='o',linestyle=' ', markersize=1,  markeredgecolor='red')

        listX=sorted(self.Y)
        listY=[x for _,x in sorted(zip(self.Y,self.X))]

        # residual function for least square is a minimisation using original (unsorted data)
        def fun(x, t, y):
            return (y - x)

        x0 = listY
        Xx = np.linspace(0,len(listX)-1,len(listX))

        #use non-linear least square
        res_robust = least_squares(fun, x0, loss='soft_l1', f_scale=0.1, args=(Xx, listY))
        print(len(res_robust.x))

        Xi=np.unique(self.Y)
        # Yi=np.poly1d(np.polyfit(self.Y, self.X, npol))(np.unique(self.Y))

        LISTX=np.asarray(listX)
        if self.flag=='T':
            plt.plot((LISTX-min(LISTX))/max(LISTX),(res_robust.x-min(res_robust.x))/max(res_robust.x), label=self.label,color=self.color, linestyle='dashed', linewidth=0.75, markersize=1)

        lstsqY=res_robust.x
        return LISTX, lstsqY

    def VTKmaxmin(self,Xi,Yi):
        Xmax=Xi[argrelextrema(Yi,np.greater)[0]]
        Ymax=Yi[argrelextrema(Yi,np.greater)[0]]
        Xmin=Xi[argrelextrema(Yi,np.less)[0]]
        Ymin=Yi[argrelextrema(Yi,np.less)[0]]
        # #
        # plt.scatter(Xmax,Ymax)
        # plt.scatter(Xmin,Ymin)
        #
        Xi=(Xi-min(Xi))/max(Xi)
        Yi=(Yi-min(Yi))/max(Yi)
        peaks,_ = find_peaks(Yi, prominence=[0.02, 1])
        results = peak_widths(Yi, peaks, rel_height=0.5)
        wid=results[0]
        widmax=max(results[0])
        widmin=widmax/4

        peaks, _ = find_peaks(Yi, width=[widmin, widmax])


        if self.flag=='T':
            plt.scatter(Xi[peaks],Yi[peaks])

        return len(Yi[peaks])

if __name__ == '__main__':
    print('this is a vtk module')
