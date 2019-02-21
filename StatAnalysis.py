#!/usr/bin/env python

###############################################################################
# Author: Dr. Asiri I.B. Obeysekara (modifications from P Salinas)
# Date: 21/02/2019
#
# For use with IC-FERST statplots to find walltime per timestep averaged over
# the last max_t timesteps. Min, max and average timesteps per #cores are the
# ouput.
#
###############################################################################

import sys
import os
from subprocess import Popen
from fluidity_tools import stat_parser as stat
import copy
import csv

output_name = 'jet_flow_fixed'
tests_list = [1,2,3,4,5,6,7,8]
nodes_list = [1, 10,20,30,40,50,60,70]
cores_list = nodes_list*36
max_t=20

wall_times = copy.deepcopy(tests_list)
TotalT = copy.deepcopy(tests_list)
TotalCores = copy.deepcopy(tests_list)
tests_list2 = copy.deepcopy(tests_list)

#Prepare the commands to run batches of simulations
commands = []
for testy in tests_list[:]:
    k = 0
    while len(testy) > k:
        dirc = 'N'+str(testy[k])
        #Retrieve the walltime for each simulation
        for t in 1:max_t
            p = stat(dirc +'/'+output_name+'.stat')["ElapsedWallTime"]["value"][-1-t]
            p2 = stat(dirc +'/'+output_name+'.stat')["ElapsedWallTime"]["value"][-1-(t+1)]
            t_deltat[i]= p2-p
            #also the total number of FPIs
            EqFPIs = sum(stat(dirc +'/'+output_name+'.stat')["Timestep"]["value"])
            # and the number of elements
            aux = stat(dirc +'/'+output_name+'.stat')["CoordinateMesh"]["elements"]
            Eles = sum(aux)/float(len(aux))#Average of number of elements

            for n, i in enumerate(wall_times):
                if i == testy[k]:
                    wall_times[n] = p
                    TotalT[n] = EqFPIs
                    TotalCores[n] = Eles/cores_list[k]
        k +=1

    #Now create a csv file with the number of cpus and times used
    with open('HPCprofiling.csv', mode='w') as walltimes_file:
        walltimes_writer = csv.writer(walltimes_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rows = zip(tests_list2,TotalCores,wall_times,TotalT)
        for row in rows:
            walltimes_writer.writerow(row)
