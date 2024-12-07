import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace


def extract_edges(edges):
    edgeX = []
    edgeY = []
    i = 153
    i = 260
    while i<316:
        j = 605
        while j>=0:
            if edges[i,j] == 255:
                edgeX.append(j)
                edgeY.append(i)
                break
            else:
                j=j-1
        i=i+1
    return edgeX, edgeY

#canny thresholds of 0 and 207 work for the psipath files to answer question 3 and a filter d=5
rawimg = cv2.imread('Data/1800um/rcphoto1810um10psi_2019.jpg')
image = cv2.imread('Data/1800um/Tare1810um10psi.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filt = cv2.bilateralFilter(gray, d=5, sigmaColor=75, sigmaSpace=75)
CanEdges = cv2.Canny(filt, 0, 207, apertureSize=5)
cv2.namedWindow('Raw Image')
cv2.namedWindow('Tared Image')
cv2.namedWindow('Edges')
while True:
    cv2.imshow('Raw Image',rawimg)
    cv2.imshow('Tared Image', gray)
    cv2.imshow('Edges', cv2.add(gray,CanEdges))
    if cv2.waitKey(1) == ord('q'):
        break

X,Y = extract_edges(CanEdges)
plt.imshow(rawimg)
plt.plot(X,Y)
plt.show()
