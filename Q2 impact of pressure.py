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

psipath = ['Data/1800um/Tare1810um10psi.jpg','Data/1800um/Tare1810um15psi.jpg','Data/1800um/Tare1810um20psi.jpg','Data/1800um/Tare1810um21psi.jpg']
#canny thresholds of 0 and 207 work for the psipath files to answer question 3 and a filter d=5

for file in psipath:
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filt = cv2.bilateralFilter(gray, d=5, sigmaColor=75, sigmaSpace=75)
    CanEdges = cv2.Canny(filt, 0, 207, apertureSize=5)
    X, Y = extract_edges(CanEdges)
    z = np.polyfit(X,Y,3)
    p = np.poly1d(z)
    dom = linspace(300,450, 450-300)

    plt.subplot(1,2,2)
    ax1 = plt.gca()
    #ax.invert_yaxis()
    plt.plot(dom,p(dom),'-',label = file)


    plt.subplot(1, 2, 1)
    ax2 = plt.gca()
    #ax.invert_yaxis()
    plt.scatter(X,Y,label = file)

#ax = plt.gca()
# invert y-axis to match image coordinates
ax1.invert_yaxis()
ax2.invert_yaxis()

# show plot
plt.legend()
plt.show()
