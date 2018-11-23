import numpy as np
import vtk
from vtk.util.numpy_support import vtk_to_numpy

#import matplotlib.pyplot as plt


def getDataTopLayerOnce(pvtu_filename, num_array):

    reader = vtk.vtkXMLPUnstructuredGridReader()
    reader.SetFileName(pvtu_filename)
    reader.Update()
    data = reader.GetOutput()
    
    # Points
    points = data.GetPoints()
    npts = points.GetNumberOfPoints()
    x = vtk_to_numpy(points.GetData())
    
    # find top layer of the structure
    top_layer_num = np.where(np.abs(x[:,1])<1e-9)[0]
    top_layer_x =x[top_layer_num,0] 
    top_layer_y =x[top_layer_num,1] 
    
#    plt.figure(0)
#    plt.plot(x[:,0],x[:,1],'b.')
#    plt.plot(x[np.where(np.abs(x[:,1])<1e-9)[0],0],x[np.where(np.abs(x[:,1])<1e-9)[0],1],'r.')
    #plt.show()
    
    # Cells
    #cells = vtk_to_numpy(data.GetCells().GetData())
    #ncells= cells.size//5
    
    
    # Field values
    n_arrays = reader.GetNumberOfPointArrays()
    if (num_array > n_arrays):
        print "the array you requested is out of the index"
#    for e0 in range(n_arrays):
#        print reader.GetPointArrayName(e0)
    print "you are reading data: " + reader.GetPointArrayName(num_array)
    
    u = vtk_to_numpy(data.GetPointData().GetArray(num_array))

    # get top-layer data
    top_layer_u     = u[top_layer_num] 
    
    # sort according x
    top_layer_x_cal = top_layer_x[top_layer_x.argsort()]
    top_layer_y_cal = top_layer_y[top_layer_x.argsort()]
    top_layer_u_cal = top_layer_u[top_layer_x.argsort()]
    
#    plt.figure(1)
#    plt.plot(top_layer_x_cal,top_layer_u1_cal*1e9*2.0,'b',label=reader.GetPointArrayName(num_array))
#    plt.legend()
#    plt.show()

    return top_layer_x_cal, top_layer_y_cal, top_layer_u_cal
