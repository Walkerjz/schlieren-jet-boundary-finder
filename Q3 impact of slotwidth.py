'''
------------------------------------------------------
This file answers Question 3
This file takes a set of tared images at different slot widths, finds points on the edge, and finds lines of best fit for each edge
The lines of best fit are printed and plotted to compare. Plots of each edge finding step are shown and compared.
------------------------------------------------------
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace

def extract_edges(edges):
    '''This function takes a canny edge detection file and returns the right-most edges arrays of X and Y coordinates'''
    # create arrays for X and Y coordinates
    edgeX = []
    edgeY = []
    # start from y = 260 and iterate through rows until row 316. These values are adjustable to avoid unwanted edge artifacts
    i = 152
    while i<300:
        # start from the right of the image and iterate across
        j = 605
        while j>=0:
            # if reach a pixel that is 255 that's an edge so save in the appropriate arrays and break out of the loop
            if edges[i,j] == 255:
                # save coordinate in appropriate array
                edgeX.append(j)
                edgeY.append(i)
                break
            else:
                # decreasing because scanning from right to left
                j=j-1
        # increasing because scanning down the image (image origin in the top left corner)
        i=i+1
        # return the edge coordinates
    return edgeX, edgeY

#list of file names images were pre-processed from raw data.
# They were cropped to standardize them, then tared, and finally some artifacts were masked out.
slotpath = ['TareMask1940um25psi.jpg','TareMask2210um25psi.jpg','TareMask2370um25psi.jpg','Tare2730um25psi.jpg']
#folder file path
path = 'Data/25psi/'

#create array to hold data from each image
edge_data =[]
#itterate through the file names in the soltpath array
for file in slotpath:
    #load image
    image = cv2.imread(path + file)
    #convert image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply a bilateral filter, these parameters were iterated on via trial and error in using the 'Canny find edge Calibration' file
    # for this application only changing the d value impacted the results
    filt = cv2.bilateralFilter(gray, d=5, sigmaColor=75, sigmaSpace=75)
    # apply the canny edge finder algorithim. Threshold values of 0 and 175 work well for the Question 3
    # data set and on of those images is used here.
    # These parameters were iterated on via trial and error in using the 'Canny find edge Calibration' file
    CanEdges = cv2.Canny(filt, 0, 175, apertureSize=5)
    #call extract_edges to pull the edges we want out from the canny edge detection
    X, Y = extract_edges(CanEdges)
    # create a plot with the image with the detected edge points overlaid
    plt.imshow(gray,cmap='gray')
    plt.scatter(X,Y)
    plt.title('Edge Detection for ' + str(file))
    plt.xlabel('x-pixels')
    plt.ylabel('y-pixels')
    plt.show()
    #run linear regression to find a line of best fit
    z = np.polyfit(X,Y,3)
    #apply regression coefficients to create a numpy polynomial
    p = np.poly1d(z)
    #save the edge points and the numpy polynomial
    edge_data.append([X,Y,p])

#create a domain to evaluate the lines of best fits across
dom = linspace(400,600, 600-400)
#create two subplots
f, (ax1, ax2) = plt.subplots(1, 2)


#iterate through file list
i = 0
while i<len(edge_data):
    #plot the lines of best fit using domain as the input
    ax2.plot(dom,edge_data[i][2](dom),'-',label = slotpath[i])
    #print out the lines of best fit
    print('Best fit for '+ str(slotpath[i]) + ' is: ')
    print(str(edge_data[i][2]))
    #add one to file index
    i = i+1
#create legend
ax2.legend()
#create plot of best fit results
ax2.set_title('Edge Line-of-Best-Fit Results')
ax2.set_ylabel('y-pixels')
ax2.set_xlabel('x-pixels')
#invert the x-axis for the lines of best fit so they are visually comparable
ax2.invert_yaxis()

#iterate through file list
i = 0
while i<len(edge_data):
    #plot each set of edge points
    ax1.scatter(edge_data[i][0],edge_data[i][1],label = slotpath[i])
    #add one to file index
    i = i+1
#invert the Y axis of the edge point data to match the graph of the lines of best fit
ax1.invert_yaxis()
#make legend
ax1.legend()
#make subplot
ax1.set_title('Edge Detection Results')
ax1.set_ylabel('y-pixels')
ax1.set_xlabel('x-pixels')

#create super title
f.suptitle('Impact of Slot Width on Jet Boundary', fontsize=16)
plt.show()

