#!/usr/bin/env python

###############################################################################
# Author: Dr. Asiri I.B. Obeysekara (modifications from P Salinas)
# Date: 21/02/2019
#
# For use with IC-FERST statplots to find a field with wall-time
#
###############################################################################

import sys
import os
from subprocess import Popen
from fluidity_tools import stat_parser as stat
import numpy as np
import copy
import csv


class StatPlot:
    def __init__(self, name, field):
        self.name = name
        self.field = field

    def splot(self, type):
        print("now plotting " + self.field + "on" + self.name)

    def fieldarray(self):
        #Prepare the commands to run batches of simulations
        p=0
        k = 0

        t=0
        T=[0.0]*max_t
        TimeS=[0.0]*max_t
        for t in range(1,max_t):
                p = stat(dirc +'/'+output_name+'.stat')["ElapsedWallTime"]["value"][-1-t]
                p2 = stat(dirc +'/'+output_name+'.stat')["ElapsedWallTime"]["value"][-1-(t-1)]
                #also the total number of time
                TimeS[t-1] = stat(dirc +'/'+output_name+'.stat')["ElapsedTime"]["value"][-1-(t-1)]
                # and the number of elements
                aux = stat(dirc +'/'+output_name+'.stat')["CoordinateMesh"]["elements"][-1-(t-1)]

                t_deltat= abs(p2-p)
                T[t-1]=t_deltat
                Eles = aux#Average of number of elements

            for n, i in enumerate(wall_times_max):
                if i == testy[k]:
                    print 'n:', n, 'and', 'i:',i
                    wall_times_max[n] = np.amax(T)
                    wall_times_min[n] = np.amin(T)
                    wall_times_avg[n] = np.mean(T)
                    TotalT[n] = np.amax(TimeS)
                    TotalCores[n] = Eles/cores_list[n]
                    k +=1
