'''
------------------------------------------------------
This file answers Question 2
This file takes a set of tared images at different pressures, finds points on the edge, and finds lines of best fit for each edge
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
    i = 260
    while i<316:
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
psipath = ['Tare1810um10psi.jpg','Tare1810um15psi.jpg','Tare1810um20psi.jpg','Tare1810um21psi.jpg']
#folder file path
path = 'Data/1800um/'

#create array to hold data from each image
edge_data =[]
#itterate through the file names in the soltpath array
for file in psipath:
    # load image
    image = cv2.imread(path + file)
    # convert image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply a bilateral filter, these parameters were iterated on via trial and error in using the 'Canny find edge Calibration' file
    # for this application only changing the d value impacted the results
    filt = cv2.bilateralFilter(gray, d=5, sigmaColor=75, sigmaSpace=75)
    # apply the canny edge finder algorithim. Threshold values of 0 and 175 work well for the Question 3
    # data set and on of those images is used here.
    # These parameters were iterated on via trial and error in using the 'Canny find edge Calibration' file
    CanEdges = cv2.Canny(filt, 0, 207, apertureSize=5)
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
dom = linspace(300,450, 450-300)
#create two subplots
plt.subplot(1,2,2)

#iterate through file list
i = 0
while i<len(edge_data):
    #plot the lines of best fit using domain as the input
    plt.plot(dom,edge_data[i][2](dom),'-',label = psipath[i])
    # print out lines of best fit
    print('Best fit for '+ str(psipath[i]) + ' is: ')
    print(str(edge_data[i][2]))
    i = i+1

#create subplot with inverted Y axis for line of best fit results
ax1 = plt.gca()
ax1.invert_yaxis()
plt.legend()
ax1.set_title('Edge Line-of-Best-Fit Results')
ax1.set_ylabel('y-pixels')
ax1.set_xlabel('x-pixels')
plt.subplot(1, 2, 1)

#iterate through file list
i = 0
while i<len(edge_data):
    #plot the edge point data to compare with line of best fit plot
    plt.scatter(edge_data[i][0],edge_data[i][1],label = psipath[i])
    i = i+1
#create subplot with inverted y-axis to show the edge point data
ax2 = plt.gca()
ax2.invert_yaxis()
ax2.set_title('Edge Detection Results')
ax2.set_ylabel('y-pixels')
ax2.set_xlabel('x-pixels')

# show plot
plt.suptitle('Impact of Pressure on Jet Boundary', fontsize=16)
plt.legend()
plt.show()