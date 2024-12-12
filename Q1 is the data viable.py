'''
------------------------------------------------------
This file answers Question 1
This file takes a raw image and a tared image and outputs a plot with points found on the edge.
------------------------------------------------------
'''



import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace

def extract_edges(edges):
    '''This function takes a canny edge detection file and returns the right-most edges arrays of X and Y coordinates'''
    #create arrays for X and Y coordinates
    edgeX = []
    edgeY = []
    #start from y = 260 and iterate through rows until row 316. These values are adjustable to avoid unwanted edge artifacts
    i = 260
    while i<316:
        # start from the right of the image and iterate across
        j = 605
        while j>=0:
            #if reach a pixel that is 255 that's an edge so save in the appropriate arrays and break out of the loop
            if edges[i,j] == 255:
                #save coordinate in appropriate array
                edgeX.append(j)
                edgeY.append(i)
                break
            else:
                #decreasing because scanning from right to left
                j=j-1
        #increasing because scanning down the image (image origin in the top left corner)
        i=i+1
    #return the edge coordinates
    return edgeX, edgeY

#load a raw image
rawimg = cv2.imread('Data/1800um/rcphoto1810um10psi_2019.jpg')
#load a Tared image, The image was tared in imageJ
image = cv2.imread('Data/1800um/Tare1810um10psi.jpg')
#convert Tared image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#apply a bilateral filter, these parameters were iterated on via trial and error in using the 'Canny find edge Calibration' file
#for this application only changing the d value impacted the results
filt = cv2.bilateralFilter(gray, d=5, sigmaColor=75, sigmaSpace=75)
#apply the canny edge finder algorithim. Threshold values of 0 and 207 work well for the Question 3
# data set and on of those images is used here
CanEdges = cv2.Canny(filt, 0, 207, apertureSize=5)
#create windows to show the raw image, tared image, and edge result.
cv2.namedWindow('Raw Image')
cv2.namedWindow('Tared Image')
cv2.namedWindow('Edges')
#show the images, have to use a loop to get it work
while True:
    cv2.imshow('Raw Image',rawimg)
    cv2.imshow('Tared Image', gray)
    cv2.imshow('Edges', cv2.add(gray,CanEdges))
    break

#call extract_edges to pull the edges we want out from the canny edge detection
X,Y = extract_edges(CanEdges)
#create a plot with the raw image with the detected edge points overlaid
plt.imshow(rawimg)
plt.xlabel('x-pixels')
plt.ylabel('y-pixels')
plt.title('edge detection (in blue)')
plt.plot(X,Y)
plt.show()

#print out X and X points because we need a metric to print out
print('Hey look! Some wild metrics have appeared! Its the-edge-points-I-detected')
print('the X coordinates ' + str(X))
print('the Y coordinates ' + str(Y))