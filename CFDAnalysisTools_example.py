import CFDAnalysisTools.VTK_filters as vt
import CFDAnalysisTools.CSV_plotter as ct
import matplotlib.pyplot as plt

SIZE=2;
SIZE2=0.8;
################## CSV Plotter
ct.Plot('file.csv','label').plotscatter(SIZE,SIZE2,'markercolor','markerstyle')

############## VTK plotter
field='TimeAverageVelocity'
vtu_number='50'
U_C=0.39; #scaling variable 1 (set to 0.0 if none)
D=0.01; #scaling variable 2 

X=[]
Y=[]

X1=0.00
X2=X1
Y1=0.00
Y2=Y1
Z1=0.00
Z2=Z1
res=1000 #resolution

N1=0 #component (if vector) to plot X(0=x,1=y,2=z)
N2=0 #component (if vector) to plot Y(0=x,1=y,2=z)

path='path'
vtuname= 'filename'+'_'+str(vtu_number)+'.pvtu'
color='black'
label='label1'
X,Y=vt.VTKfilter(path, vtuname, field).Line(X1,X2,Y1,Y2,Z1,Z2,res)
vt.Plotter(X,Y,label,color).VTKplot(X1,0,D,U_C, N1, N2)


###
plt.xlabel('x')
plt.ylabel('y')
plt.title('Title')
plt.legend()
plt.show()
