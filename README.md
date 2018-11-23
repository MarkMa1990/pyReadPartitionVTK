# pyReadPartitionVTK
Read *.pvtu data, same function as what Paraview did

This work is to solve the problem to read time series data in *.pvtu* format. Paraview provies rather powerful visulization methods to show the scientific data. However, we find it has difficulties in plotting line data of series time in a single 3D figure (e.g. X-axis=x, Y-axis=time, Z-axis=data). To do so, one has to come back to read the vtk file and retrive the data as you want. By looping the time series and assembling the line data to a single matrix, one could save it and visualize in other plotting packages such as matplotlib.

## To run
<pre><code> python getTimeData.py
</code></pre>

## References:
[1]. How to write VTK files in parallel. http://rotorbit.blogspot.com/2017/02/how-to-write-vtk-files-in-parallel.html

[2]. https://www.vtk.org/Wiki/VTK/Examples/Python

[3]. https://www.paraview.org/Wiki/ParaView/ParaView_Readers_and_Parallel_Data_Distribution

[4]. Read VTK file and plot with matplotlib. https://perso.univ-rennes1.fr/pierre.navaro/read-vtk-with-python.html
