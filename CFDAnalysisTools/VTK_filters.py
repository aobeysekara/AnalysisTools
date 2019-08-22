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


class VTKfilter():
    def __init__(self, path, vtuname, field):
        self.path=path
        self.vtuname=vtuname
        self.field=field

    def Line(self,X1,X2,Y1,Y2,Z1,Z2,res):
        parallel=False
        if self.vtuname.endswith(".pvtu"):
            parallel=True
        ############################ Plot from Numerical results
        #NAME OF THE VARIABLE YOU WANT TO EXTRACT DATA FROM
        path=self.path
        data_name_field = self.field
        ############ initial
        AutoVTU=2
        AutoNumber = 0
        if AutoVTU==1:
            for files in os.listdir(path):
                if files.endswith(".vtu"):
                    pos = files.rfind('_')
                    pos2 = files.rfind('.')
                    AutoFile = files[:pos]
                    AutoNumber = max(AutoNumber, int(files[pos+1:pos2]))
            AutomaticFile = AutoFile
            AutomaticVTU_Number = AutoNumber
            if (len(sys.argv)>1):
                filename   = sys.argv[1]
                vtu_number = int(sys.argv[2])
            else:
                filename = AutomaticFile
                vtu_number = int(AutomaticVTU_Number)
            # serial
            if (parallel==True):
                reader = vtk.vtkXMLPUnstructuredGridReader()
                reader.SetFileName(filename+'_'+str(vtu_number)+'.pvtu')
            else:
                reader = vtk.vtkXMLUnstructuredGridReader()
                reader.SetFileName(filename+'_'+str(vtu_number)+'.vtu')
        else:
            if (parallel==True):
                reader = vtk.vtkXMLPUnstructuredGridReader()
            else:
                reader = vtk.vtkXMLUnstructuredGridReader()
            reader.SetFileName(self.path+self.vtuname)
        #reader.Update()
        ugrid = reader.GetOutputPort()
        #Initial and last coordinate of the probe
        x0 = X1
        x1 = X2
        y0 = Y1 # 1.0/float(NUMBER)
        y1 = Y2
        z0 = Z1
        z1 = Z2
        #Resolution of the probe
        resolution = res
        #ugrid.Update()
        ###########Create the probe line#############
        Field=[]
        detector = []
        hx = (x1 - x0) / resolution
        hy = (y1 - y0) / resolution
        hz = (z1 - z0) / resolution

        for i in range(resolution+1):
            detector.append([hx * i + x0, hy * i + y0, hz * i + z0])

        #print 'using',len(detector),'detectors'
        points = vtk.vtkPoints()
        points.SetDataTypeToDouble()

        for i in range(len(detector)):
            points.InsertNextPoint(detector[i][0], detector[i][1], detector[i][2])

        detectors = vtk.vtkPolyData()
        detectors.SetPoints(points)
        ###########Create the probe line end#############
        probe = vtk.vtkProbeFilter()
        probe.SetInputConnection(ugrid)
        probe.SetSourceConnection(ugrid)
        probe.SetInputData(detectors)
        probe.Update()

        data = probe.GetOutput()
        for j in range(points.GetNumberOfPoints()):
            #print(data.GetPointData().GetScalars("vtkValidPointMask").GetValue(j))
            Field.append( data.GetPointData().GetScalars(data_name_field).GetTuple(j))
        return detector, Field


class Plotter():
    def __init__(self, X, Y, label, color):
        self.X = X #
        self.Y = Y #currently a vector array
        self.label=label
        self.color=color

    def VTKplot(self, Xi,Yi,Xd,Yd):
        #Xi and Xd are the numerator and denomiator scaling factors, respectively
        #Yi and Yd are the numerator and denomiator scaling factors, respectively
    	xN = []
    	yN = []
        for i in range(len(self.X)):
            if (float(self.Y[i][0]) != 0):
            	xN.append((float(self.X[i][0])-Xi)/Xd)#+0.5)#In this test case the origin is in -0.5
            	yN.append((float(self.Y[i][0])-Yi)/Yd)
        print(self.label)
        plt.plot(xN, yN, label=self.label,color=self.color, linestyle='dashed', linewidth=0.5, markersize=1)



if __name__ == '__main__':
    print('this is a module')