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


class DataAnalysis():
    def __init__(self, X, Y, label, color):
        self.X = X #
        self.Y = Y #currently a vector array
        self.label=label
        self.color=color

    def VTKCurveFit(self, npol):
        from scipy.optimize import least_squares

        #original data
        plt.plot(self.Y,self.X, marker='o',linestyle=' ', markersize=1,  markeredgecolor='red')

        listX=sorted(self.Y)
        listY=[x for _,x in sorted(zip(self.Y,self.X))]

        # plt.plot(listX,listY)
        def fun(x, t, y):
            return (y - x)

        x0 = listY
        Xx = np.linspace(0,len(listX)-1,len(listX))

        res_robust = least_squares(fun, x0, loss='soft_l1', f_scale=0.1, args=(Xx, listY))
        print(len(res_robust.x))

        Xi=np.unique(self.Y)
        # Yi=np.poly1d(np.polyfit(self.Y, self.X, npol))(np.unique(self.Y))

        plt.plot(listX,res_robust.x, label=self.label,color=self.color, linestyle='dashed', linewidth=0.75, markersize=1)

        lstsqY=res_robust.x
        return Xi, lstsqY

    def VTKmaxmin(self,Xi,Yi):
        Xmax=Xi[argrelextrema(Yi,np.greater)[0]]
        Ymax=Yi[argrelextrema(Yi,np.greater)[0]]
        Xmin=Xi[argrelextrema(Yi,np.less)[0]]
        Ymin=Yi[argrelextrema(Yi,np.less)[0]]

        plt.scatter(Xmax,Ymax)
        plt.scatter(Xmin,Ymin)


if __name__ == '__main__':
    print('this is a vtk module')
