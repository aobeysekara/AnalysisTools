import CFDAnalysisTools.VTK_filters as vt
import CFDAnalysisTools.CSV_plotter as ct


SIZE=2;
SIZE2=0.8;
################## CSV Plotter
ct.Plot('file.csv','label').plotscatter(SIZE,SIZE2,'markercolor','markerstyle')

############## VTK plotter
field='TimeAverageVelocity'
vtu_number='50'
U_C=0.39; #speed
D=0.01; #diameter

X=[]
Y=[]

X1=0.05
X2=X1+10*D
Y1=0.15
Y2=Y1
Z1=0.015725
Z2=Z1
res=1000 #resolution

path='path'
vtuname= 'filename'+'_'+str(vtu_number)+'.pvtu'
color='black'
label='label1'
X,Y=vt.VTKfilter(path, vtuname, field).Line(X1,X2,Y1,Y2,Z1,Z2,res)
vt.Plotter(X,Y,label,color).VTKplot(X1,0,D,U_C)


###
plt.xlabel('x')
plt.ylabel('y')
plt.title('Title')
plt.legend()
plt.show()
