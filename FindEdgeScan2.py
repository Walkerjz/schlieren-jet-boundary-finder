import cv2
import matplotlib.pyplot as plt
import numpy as np



def edge_at_row(img, column):
    """finds edge point in a column."""
    data = img[:,column]
    threshold = 10/306*(column-300)+60
        #np.mean(image[280:514, 326:594]))
    c=0
    i=0
    while i<367:
        if data[i] > threshold:
            break
        i=i+1

    while i<367:
        if data[i] < threshold:
            break
        i=i+1
    edge = [i,column]

    return edge



# Create a window with trackbars
cv2.namedWindow('My edge detection')
cv2.createTrackbar('Column', 'My edge detection', 0, 605, lambda x: x)


while True:
    # Get the current trackbar values
    column = cv2.getTrackbarPos('Column', 'My edge detection')
    image = cv2.imread('Data/rcphoto2370um30psi_2019.jpg')
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Canny edge detection
    img = cv2.bilateralFilter(img,d=2, sigmaColor=75, sigmaSpace=75)

    edge = edge_at_row(img, column)
    black = np.zeros((369,606),dtype=np.uint8)
    black[edge[0],edge[1]] = 255
    # Display the result
    cv2.imshow('Scan Detection', cv2.add(img, black))
    #open cv make a black image of zeros then insert the edge at a point

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()