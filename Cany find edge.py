import cv2
import numpy as np

"""
Where do canny thresholds come from? can I set them by averaging the white space?
"""



def apply_canny(image, low_threshold, high_threshold):
    """Applies Canny edge detection with adjustable thresholds."""

    # Convert to grayscale if necessary
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    # Apply Canny edge detection
    #filt = cv2.GaussianBlur(gray, (7,7),0)
    filt = cv2.bilateralFilter(gray,d=12, sigmaColor=1000, sigmaSpace=75)

    edges = cv2.Canny(filt, low_threshold, high_threshold, apertureSize=5)
    """L2gradient=True,"""

    return edges, gray

# Read the image
path = ['Data/rcphoto2370um30psi_2019.jpg','Data/rcphoto2270um24psi_2016.jpg','Data/rcphoto2370um10psi_2019.jpg']
image = cv2.imread(path[2])

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

    # Display the result
    cv2.imshow('Canny Edge Detection', cv2.add(edges,grey))


    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

print(edges)
cv2.destroyAllWindows()