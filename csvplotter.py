#!/usr/bin/env python

###############################################################################
# Author: Dr. Asiri I.B. Obeysekara (modifications from P Salinas)
# Date: 20/08/2019
#

#
###############################################################################

import sys
import os
import numpy as np
import csv
import vtk
import sys
from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d

class CSVplotter(object):
    filtered = []

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

    def __init__(self, file):
        self.file = file

    def csv_plotter(name):
        	x,y = for row in in CSVplotter(name)

        	line = plt.Line2D(x, y, color='red', linewidth=2)
        	#line.text.set_color('red')
        	#line.text.set_fontsize(16)
        	ax[0].add_line(line)
        	line3 = plt.Line2D(x, yp, color='red', linewidth=2)
        	ax[1].add_line(line3)


        	plt.show()




if __name__ == "__main__":
    GeneralPlotter(name)
