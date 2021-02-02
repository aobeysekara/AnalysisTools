# AnalysisTools
(WIP)
Python tools and examples for analysis of numerical results (such as from IC-FERST/Fluidity) that use VTK (such as vtu and pvtu files)
- Works for parallel and serial vtk output files
- Display results with matplotlib plot
- Main classes and VTK scripts are located in directory <CFDAnalysisTools>

Step 1:
- Fork 

Step 2:
- Check which version of VTK you are using (tested with vtk6)
- Run example as in CFDAnalysisTools_example (which compares experimental results in a csv file with results derived from a line probe in VTK) 




1. EXAMPLE (vtk line data and plot):

Field and file data: 
```
field='Field_name'
vtu_number='50'
U_C=0.39; #scaling variable 1 (set to 0.0 if none)
D=0.01; #scaling variable 2 
```

Setting coordinates:
```
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
```
Name of the file:
```
path='path'
vtuname= 'filename'+'_'+str(vtu_number)+'.pvtu'
color='black'
label='label1'
```
Filter f(x):
```
X,Y=vt.VTKfilter(path, vtuname, field).Line(X1,X2,Y1,Y2,Z1,Z2,res)
```

Plot f(x):
```
vt.Plotter(X,Y,label,color).VTKplot(X1,0,D,U_C, N1, N2)

```
Display plot:
```
plt.xlabel('x')
plt.ylabel('y')
plt.title('Title')
plt.legend()
plt.show()
```
Run the test case using 'python CFDAnalysisTools_test.py' in the test folder to check if this works in your system
