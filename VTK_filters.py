#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import vtk
from math import *
from scipy import interpolate

Xi=0.05
Yi=0.15
Zi=0.015725
U_C=0.39;
D=0.01;
SIZE=2;
SIZE2=0.8;

class VTKfilter():
    def __init__(self, path, vtuname, field,label):
        self.path=path
        self.vtuname=vtuname
        self.field=field
        self.label=label

    def WakeVel(self,color):
        showPlot = True;
        parallel=False
        if self.vtuname.endswith(".pvtu"):
            parallel=True
        if (showPlot):
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
                else:
                    reader = vtk.vtkXMLUnstructuredGridReader()
                reader.SetFileName(filename+'_'+str(vtu_number)+'.pvtu')
            else:
                if (parallel==True):
                    reader = vtk.vtkXMLPUnstructuredGridReader()
                else:
                    reader = vtk.vtkXMLUnstructuredGridReader()
                reader.SetFileName(self.path+self.vtuname)
            #reader.Update()
            ugrid = reader.GetOutputPort()
            #Initial and last coordinate of the probe
            x0 = Xi
            x1 = Xi+10*D
            y0 = Yi # 1.0/float(NUMBER)
            y1 = y0
            z0 = Zi
            z1 = z0
            #Resolution of the probe
            resolution = 1000
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

        	xN = []
        	yN = []
            for i in range(len(detector)):
                if (float(Field[i][0]) != 0):
                	xN.append((float(detector[i][0])-x0)/D)#+0.5)#In this test case the origin is in -0.5
                	yN.append(float(Field[i][0])/U_C)
            print(self.label)
            plt.plot(xN, yN, label=self.label,color=color, linestyle='dashed', linewidth=0.5, markersize=1)



if __name__ == '__main__':
    print('this is a module')