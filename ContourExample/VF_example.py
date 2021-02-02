import CFDAnalysisTools.VTK_filters as vt
import CFDAnalysisTools.CSV_plotter as ct
import CFDAnalysisTools.DataFit as dt
import matplotlib.pyplot as plt


################## CSV Plotter
SIZE=0.5;
SIZE2=0.8;
# ct.Plot('file.csv','label').plotscatter(SIZE,SIZE2,'markercolor','markerstyle')

############## VTK plotter
field='phase1::PhaseVolumeFraction'

X=[]
Y=[]
color='black'
label='label1'
path=''
#path='/media/Data2/ASIRI/WORK/AMCG/ANDREAS/CFDAnalysisTools/DataFileLong/'
numpeaks=[]

N=2
Nmax=N+1
for i in range(N,Nmax):
    print(i)
    flag='F'
    vtu_number=i
    if i==N:
        flag='T'
    vtuname= 'TenthPcOrigFIXMesh'+'_'+str(vtu_number)+'.pvtu'
    #vtuname= 'TenthPcVisc10k'+'_'+str(vtu_number)+'.pvtu'


    #X,Y=vt.VTKfilter(path, vtuname, field).Line(X1,X2,Y1,Y2,Z1,Z2,res)
    # vt.Plotter(X,Y,label,color).VTKplot(X1,0,D,U_C,0,0)

    coords,X,Y=vt.VTKfilter(path, vtuname, field).Contour(0.32)
    Xi,Yi=dt.DataAnalysis(X,Y,label,color,flag).VTKCurveFit(21)
    numpeaks.append(dt.DataAnalysis(X,Y,label,color,flag).VTKmaxmin(Xi,Yi))
    if flag=='F':
        plt.plot(numpeaks)
print(numpeaks)
# plt.scatter(Y,X)




###
plt.xlabel('x')
plt.ylabel('y')
plt.title('Title')
#plt.legend()
plt.show()
