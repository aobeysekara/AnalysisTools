import matplotlib.pyplot as plt
import os
import sys

path = os.getcwd()
path2= os.path.dirname(path)

try:
    sys.path.index(path2) 
except ValueError:
    sys.path.append(path2) 



import CFDAnalysisTools.VTK_filters as vt
import CFDAnalysisTools.CSV_plotter as ct

SIZE=2;
SIZE2=0.8;
################## CSV Plotter
ct.Plot(path + '/results/LaurencoShih_streamwisewake.csv','Laurenco & Shih (1993)').plotscatter(SIZE,SIZE2,'black','x')


############## VTK plotter
field='TimeAverageVelocity'
N=0 #X-axis
vtu_number='230'

U_C=0.39;
D=0.01;

C_X=0.05
C_Y=0.15
C_Z=0.015725

X=[]
Y=[]

X1=0.05
X2=X1+10*D
Y1=0.15
Y2=Y1
Z1=0.015725
Z2=Z1
res=1000#resolution



vtuname= '/results/3D_FlowPastCylinderExample'+'_'+str(vtu_number)+'.pvtu'
color='blue'
label='example'
X,Y=vt.VTKfilter(path, vtuname, field).Line(X1,X2,Y1,Y2,Z1,Z2,res)
vt.Plotter(X,Y,label,color).VTKplot(C_X,0,D,U_C,N,0)


FS=8

### formatting
plt.xlabel('x/D',fontsize=FS)
plt.ylabel('$u_x/U_c$',fontsize=FS)
plt.title('Streamwise Velocity along wake-line (validation)'+'VTU'+str(vtu_number),fontsize=FS)
plt.legend()
plt.legend( frameon=False, labelspacing=1, title='Result',fontsize=FS)
plt.tick_params(labelsize=FS)
plt.show()
