import cv2
import matplotlib.pyplot as plt
import numpy as np



def find_edge(img):
    #filter the image
    filt = cv2.bilateralFilter(img, d=5, sigmaColor=75, sigmaSpace=75)
    #generate a black image to put our edge points on
    edge = np.zeros((369, 606), dtype=np.uint8)
    # set a column value
    col = 0
    while col<605:
        #threshold changes linearly across the image kinda like this
        threshold = 9 / 306 * (col - 300) + 60
        #row value set to zero before each column itterated through
        i=0
        #grab a vertical row
        data = filt[:, col]
        #itterate through the column untill its above the threshold
        while i<367:
            if data[i] > threshold:
                break
            i=i+1
        #itterate through the column until the data goes below the threshold
        while i<367:
            if data[i] < threshold:
                break
            i=i+1
        #make the edge a point in the edge image/matrix
        edge[i,col] = 255
        #go to the next column
        col = 1+ col

    return edge



# Create a window with trackbars
cv2.namedWindow('My edge detection')
#cv2.createTrackbar('Column', 'My edge detection', 0, 605, lambda x: x)
path = ['Data/rcphoto2370um30psi_2019.jpg','Data/rcphoto2270um24psi_2016.jpg','Data/rcphoto2370um10psi_2019.jpg']
image = cv2.imread(path[2])
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
while True:

    edge = find_edge(img)
    # Display the result
    cv2.imshow('Scan Detection', cv2.add(img, edge))
    #open cv make a black image of zeros then insert the edge at a point

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()