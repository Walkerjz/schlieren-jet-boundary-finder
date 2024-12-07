import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace


def extract_edges(edges):
    edgeX = []
    edgeY = []
    i = 152
    while i<300:
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

slotpath = ['TareMask1940um25psi.jpg','TareMask2210um25psi.jpg','TareMask2370um25psi.jpg','Tare2730um25psi.jpg']
#canny thresholds of 0 and 154 work for the slotpath files to answer question 2 and a filter d=5
path = 'Data/25psi/'

edge_data =[]
for file in slotpath:
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
f, (ax1, ax2) = plt.subplots(1, 2)
#plt.subplot(1,2,2)
ax2.invert_xaxis()
#plt.xlim((max(X), min(X)))
i = 0
while i<len(edge_data):
    ax2.plot(dom,edge_data[i][2](dom),'-',label = slotpath[i])
    print('Best fit for '+ str(slotpath[i]) + ' is: ')
    print(str(edge_data[i][2]))
    i = i+1

ax2.legend()

#plt.subplot(1, 2, 1)
i = 0
while i<len(edge_data):
    ax1.scatter(edge_data[i][0],edge_data[i][1],label = slotpath[i])
    i = i+1
ax1.invert_yaxis()
ax1.legend()

plt.show()

