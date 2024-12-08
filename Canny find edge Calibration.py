import cv2
import numpy as np

def apply_canny(image, low_threshold, high_threshold):
    """Applies Canny edge detection with adjustable thresholds."""

    # Convert to grayscale if necessary
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    # Apply Canny edge detection

    #d=12 works well for Data/rcphoto2370um30psi_2019.jpg
    #filter the image
    filt = cv2.bilateralFilter(gray,d=5, sigmaColor=1000, sigmaSpace=75)

    #apply the canny image detection and return image of the edges found
    edges = cv2.Canny(filt, low_threshold, high_threshold, apertureSize=5)
    # return the grayscale image and edges
    return edges, gray

#Path is a list of different files to play with
path = ['Data/rcphoto2370um30psi_2019.jpg','Data/rcphoto2270um24psi_2016.jpg','Data/rcphoto2370um10psi_2019.jpg', 'Data/TARED1810um22psi.jpg']

#psipath is a list of images with the same slot width and changing pressure
psipath = ['Data/1800um/Tare1810um10psi.jpg','Data/1800um/Tare1810um15psi.jpg','Data/1800um/Tare1810um20psi.jpg','Data/1800um/Tare1810um21psi.jpg']
#canny thresholds of 0 and 207 work for the psipath files to answer question 3 and a filter d=5

#slotpath is a list of images with the same pressure and changing slotwidth
slotpath = ['Data/25psi/TareMask1940um25psi.jpg','Data/25psi/TareMask2210um25psi.jpg','Data/25psi/Tare2370um25psi.jpg','Data/25psi/Tare2730um25psi.jpg']
#canny thresholds of 0 and 175 work for the slotpath files to answer question 2 and a filter d=5

#read image from one of the arrays
image = cv2.imread(psipath[0])

# Create a window with trackbars
cv2.namedWindow('Canny Edge Detection')
cv2.createTrackbar('Low Threshold', 'Canny Edge Detection', 0, 255, lambda x: x)
cv2.createTrackbar('High Threshold', 'Canny Edge Detection', 0, 255, lambda x: x)
while True:
    # Get the current trackbar values
    low_threshold = cv2.getTrackbarPos('Low Threshold', 'Canny Edge Detection')
    high_threshold = cv2.getTrackbarPos('High Threshold', 'Canny Edge Detection')


    # Apply Canny edge detection
    edges, grey = apply_canny(image, low_threshold, high_threshold)

    # Display the result adding the gray image and edges
    cv2.imshow('Canny Edge Detection', cv2.add(edges,grey))

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()