from cProfile import label

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
                #edgeX = np.append(j)
                #edgeY = np.append(i)
                edgeX.append(j)
                edgeY.append(i)
                break
            else:
                j=j-1
        i=i+1
    return edgeX, edgeY

psipath = ['Tare1810um10psi.jpg','Tare1810um15psi.jpg','Tare1810um20psi.jpg','Tare1810um21psi.jpg']
#canny thresholds of 0 and 207 work for the psipath files to answer question 3 and a filter d=5
path = 'Data/1800um/'

edge_data =[]
for file in psipath:
    image = cv2.imread(path + file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filt = cv2.bilateralFilter(gray, d=5, sigmaColor=75, sigmaSpace=75)
    CanEdges = cv2.Canny(filt, 0, 207, apertureSize=5)
    X, Y = extract_edges(CanEdges)
    plt.imshow(gray,cmap='gray')
    plt.scatter(X,Y)
    plt.show()
    z = np.polyfit(X,Y,3)
    p = np.poly1d(z)
    edge_data.append([X,Y,p])



dom = linspace(300,450, 450-300)
thing = edge_data[0][2]
plt.subplot(1,2,2)
plt.plot(dom,edge_data[0][2](dom),'-',label = file,)

plt.subplot(1, 2, 1)

plt.scatter(X,Y,label = file)

ax1 = plt.gca()
ax2 = plt.gca()
ax1.invert_yaxis()
ax2.invert_yaxis()
# show plot
plt.legend()
plt.show()
