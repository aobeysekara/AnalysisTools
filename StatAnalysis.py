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
import numpy as np
import copy
import csv

output_name = 'jet_flow_fixed'
tests_list =[2,3] #[1,2,3,4,5,6,7,8]
tests_list.sort(key=int)
sub_tests = [[0] * 0 for i in range(len(tests_list))]
max_t=[1,2]
nodes_list =[10,20] #[1, 10,20,30,40,50,60,70]
cores_list = [x*36 for x in nodes_list]
print cores_list
max_t=20

wall_times_max = copy.deepcopy(tests_list)
wall_times_min = copy.deepcopy(tests_list)
wall_times_avg = copy.deepcopy(tests_list)

TotalT = copy.deepcopy(tests_list)
TotalCores = copy.deepcopy(tests_list)
tests_list2 = copy.deepcopy(tests_list)

k = -1
while len(tests_list) > 0:
    k +=1
    #Start from last, as it is the biggest
    p = tests_list[-1]
    sub_tests[k].append(p)
    tests_list.remove(p)
    #Used cpus so far
    remaining_tests = int(sub_tests[k][-1])
    #Now check how many from the start fit
    for x in tests_list[:]:
        if (remaining_tests - int(x) > 0):
            sub_tests[k].append(x)
            remaining_tests -= int(x)
            tests_list.remove(x)

#Prepare the commands to run batches of simulations
commands = []
for testy in sub_tests[:]:
    k = 0
    while len(testy) > k:
        dirc = 'N'+str(testy[k])
        tests_list2[k]=dirc
        #Retrieve the walltime for each simulation
        t=0
        T=[0.0]*20
        for t in range(0,20):
            p = stat(dirc +'/'+output_name+'.stat')["ElapsedWallTime"]["value"][-1-t]
            p2 = stat(dirc +'/'+output_name+'.stat')["ElapsedWallTime"]["value"][-1-(t+1)]
            t_deltat= p-p2
            T[t]=t_deltat
            #also the total number of time
            EqFPIs = stat(dirc +'/'+output_name+'.stat')["ElapsedTime"]["value"][-1-t]
            # and the number of elements
            aux = stat(dirc +'/'+output_name+'.stat')["CoordinateMesh"]["elements"][-1]
            Eles = aux#Average of number of elements
            for n, i in enumerate(wall_times_max):
                if i == testy[k]:
                    wall_times_max[n] = np.amax(T)
                    wall_times_min[n] = np.amin(T)
                    wall_times_avg[n] = np.mean(T)
                    TotalT[n] = EqFPIs
                    TotalCores[n] = Eles/cores_list[k]
        k +=1
        T_max=max(T)
        T_min=min(T)
        T_avg=np.mean(T)
        print T_max, T_min, T_avg
        print wall_times_avg
    #Now create a csv file with the number of cpus and times used (make this into a function)
    with open('HPCprofiling.csv', mode='w') as walltimes_file:
        walltimes_writer = csv.writer(walltimes_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rows = zip(tests_list2,TotalCores,wall_times_max,wall_times_min,wall_times_avg,TotalT)
        for row in rows:
            walltimes_writer.writerow(row)
