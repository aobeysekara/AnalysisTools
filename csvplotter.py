#!/usr/bin/env python

###############################################################################
# Author: Dr. Asiri I.B. Obeysekara (modifications from P Salinas)
# Date: 20/08/2019
#

#
###############################################################################

import sys
import os
import csv
import vtk
from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.interpolate import interp1d

class CSVplotter(object):
    #parent class of data reader
    def __init__(self, file):
        self.file=file

    def read_csv_file(self):
        try:
            with open(self.file, "r") as f:
                self.reader = [row for row in csv.reader(f, delimiter= " ")]
                return self.reader
        except IOerror as err:
            print("I/O error ({0}):{1}".format(errno, strerror))
        return

    def write_csv_file(self):
        try:
            with open(self.file, "w") as f:
                self.writer = [row for row in csv.writer(f, delimiter= " ",
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)]
                return self.writer
        except IOerror as err:
            print("I/O error ({0}):{1}".format(errno, strerror))
        return


    def get_num_rows(self):
        print (sum(1 for tow in self.reader))


class GeneralPlotter(object):
#this is the general plotter class, this will contain plotting tools
#for statfiles, csv and vtk
    def __init__(self, file):
        self.file = file

    def csv_plotter(self):
            filename, file_extension = os.path.splitext(self.file)
            if file_extension == '.csv':
                type=1
            elif file_extension == '.stat':
                type=2
            elif file_extension == '.vtu':
                type=3
            else:
                print("Error: Unrecognised file type {0}".format(file_extension))
                sys.exit()

            fig, ax = plt.subplots(1, sharex=True)
            if type == 1: #this is for CSV
                x,y = for row in in CSVplotter(self.file)
            else:
                print("ONLY READING CSV AT THE MOMENT")
                sys.exit()

        	line = plt.Line2D(x, y, color='red', linewidth=2)
        	ax[0].add_line(line)

        	plt.show()



if __name__ == "__main__":
    GeneralPlotter(name)
