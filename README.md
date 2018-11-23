# pyReadPartitionVTK
read *.pvtu data, same function as what Paraview did

This work is to solve the problem to read time series data in *.pvtu* format. Paraview provies rather powerful visulization methods to show the scientific data. However, we find it has difficulties in plotting line data of series time in a single 3D figure (e.g. Xaxis=x, Yaxis=time, Zaxis=data). To do so, one has to come back to read the vtk file and retrive the data as you want. By looping the time series and assembling the line data to a single matrix, one could save it and visualize in other plotting packages such as matplotlib.
