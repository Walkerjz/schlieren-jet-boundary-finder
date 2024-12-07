import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve


def edge_at_row(img, row):
    """finds edge point in a row."""
    # grab a row from the image
    data = img[row, :]
    # smooth data with a moving average
    data = convolve(data,np.ones(30)/30)
    #itterate backwards through a row
    i = 605
    avg = data[605]
    num = 1
    while True:
        #calculate a running average
        runavg = np.sum(data[i-1:605])/(605-(i-1))
        if abs(data[i] - runavg) >=5:
            return [row,i]

        if i == 0:
            return [0,0]
            break
        else:
            i = i - 1



# Create a window with trackbars
cv2.namedWindow('My edge detection')
cv2.createTrackbar('Column', 'My edge detection', 0, 368, lambda x: x)


while True:
    # Get the current trackbar values
    column = cv2.getTrackbarPos('Column', 'My edge detection')
    image = cv2.imread('Data/rcphoto2370um30psi_2019.jpg')
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Canny edge detection
    #img = cv2.bilateralFilter(img,d=12, sigmaColor=75, sigmaSpace=75)

    edge = edge_at_row(img, column)
    black = np.zeros((369,606),dtype=np.uint8)
    black[edge[0],edge[1]] = 255
    # Display the result
    cv2.imshow('Scan Detection', cv2.add(img, black))
    #open cv make a black image of zeros then insert the edge at a point
    if cv2.waitKey(1) == 27:  # hit escape to quit
        break
