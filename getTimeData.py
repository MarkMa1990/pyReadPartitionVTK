
import numpy as np

import getFileName as gfn
import getDataVTKOnce as gdvtk

# foldname of the data
dirname0 = "./data_70um/"

# get filenames of pvtu
folds0, files0 = gfn.get_filefoldnames(dirname0)
pvtu_filenames0 = gfn.get_pvtuNames(files0)

top_layer_x_time = np.array([])
top_layer_y_time = np.array([])

top_layer_u1_time = np.array([])
top_layer_u2_time = np.array([])
top_layer_u3_time = np.array([])

timesteps00 = np.array([])

# if first time append to matrix
numcal = 0

for pvtu_filename in pvtu_filenames0:
    x1_data, y1_data, u1_data = gdvtk.getDataTopLayerOnce(dirname0+pvtu_filename,0)
    x2_data, y2_data, u2_data = gdvtk.getDataTopLayerOnce(dirname0+pvtu_filename,1)
    x3_data, y3_data, u3_data = gdvtk.getDataTopLayerOnce(dirname0+pvtu_filename,2)
   
    if(numcal == 0):
        top_layer_x_time  = np.append(top_layer_x_time,  x1_data, axis=0)
        top_layer_y_time  = np.append(top_layer_y_time,  y1_data, axis=0)
        top_layer_u1_time = np.append(top_layer_u1_time, u1_data, axis=0)
        top_layer_u2_time = np.append(top_layer_u2_time, u2_data, axis=0)
        top_layer_u3_time = np.append(top_layer_u3_time, u3_data, axis=0)
    else:
        top_layer_x_time = np.vstack([top_layer_x_time, x1_data])
        top_layer_y_time = np.vstack([top_layer_y_time, y1_data])
        top_layer_u1_time = np.vstack([top_layer_u1_time, u1_data])
        top_layer_u2_time = np.vstack([top_layer_u2_time, u2_data])
        top_layer_u3_time = np.vstack([top_layer_u3_time, u3_data])

    # get time step
    stepcal = np.int32(pvtu_filename.split("-")[1].split(".")[0])
    timesteps00 = np.append(timesteps00,np.array([stepcal]),axis=0)

    numcal += 1

    print "you are reading files of number: " + str(numcal)
    print "the name is: " + dirname0 + pvtu_filename
    print ""


#print timesteps00
#print top_layer_u1_time
#
#import matplotlib.pyplot as plt
#
#plt.figure(0)
#plt.plot(top_layer_x_time[0,:],top_layer_u2_time[0,:],'b-',label="timestep at "+str(timesteps00[0]))
#plt.plot(top_layer_x_time[1,:],top_layer_u2_time[1,:],'g-',label="timestep at "+str(timesteps00[1]))
#plt.plot(top_layer_x_time[2,:],top_layer_u2_time[2,:],'r-',label="timestep at "+str(timesteps00[2]))
#plt.legend()
#plt.show()
