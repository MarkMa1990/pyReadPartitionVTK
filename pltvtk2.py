import numpy as np
import vtk
from vtk.util.numpy_support import vtk_to_numpy

import matplotlib.pyplot as plt

reader = vtk.vtkXMLPUnstructuredGridReader()
reader.SetFileName("./data_70um/solution-0196400.pvtu")
reader.Update()
data = reader.GetOutput()

print reader.GetInformation()

print reader.GetPointArrayName(1)


# Points
points = data.GetPoints()
npts = points.GetNumberOfPoints()
x = vtk_to_numpy(points.GetData())

print x[:,0]
print x[:,1]

top_layer_num = np.where(np.abs(x[:,1])<1e-9)[0]
top_layer_x =x[top_layer_num,0] 
top_layer_y =x[top_layer_num,1] 
#print np.where(np.abs(x[:,1])<1e-9)
#print x[np.where(np.abs(x[:,1])<1e-9)[0],1]
#print x[np.where(np.abs(x[:,1])<1e-9)[0],0]

plt.figure(0)
plt.plot(x[:,0],x[:,1],'b.')
plt.plot(x[np.where(np.abs(x[:,1])<1e-9)[0],0],x[np.where(np.abs(x[:,1])<1e-9)[0],1],'r.')
#plt.show()

# Cells

#cells = vtk_to_numpy(data.GetCells().GetData())
#ncells= cells.size//5


# Field values
n_arrays = reader.GetNumberOfPointArrays()
for e0 in range(n_arrays):
    print reader.GetPointArrayName(e0)

u = vtk_to_numpy(data.GetPointData().GetArray(1))

# sort according x
top_layer_x_cal  = top_layer_x[top_layer_x.argsort()]
top_layer_u1     = u[top_layer_num] 
top_layer_u1_cal = top_layer_u1[top_layer_x.argsort()]

plt.figure(1)
plt.plot(top_layer_x_cal,top_layer_u1_cal*1e9*2.0,'b',label=reader.GetPointArrayName(1))
plt.legend()
plt.show()
