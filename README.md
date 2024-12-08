# The Challenge:
This code is designed to extract the boundary of a supersonic jet of air moving over a Coanda surface from Schlieren images.
The data set is a set of images of the jet boundary taken at different slot widths and pressures.
Schlieren is a technique to take images of transparent media such as fluid flow.

Below is a sample jet. The black curved part of the image is the Coanda Flare and the brighter part of the image is air.
The jet can be seen in the brightest parts of the image. It follows the curved surface due to the Coanda effect.
The jet starting location is labeled as well as the dimension considered to be the jet boundary.
![img_3.png](img_3.png)

This data was taken to determine a polynomial of the jet boundary and also to understand the shock cell structure.
Understanding the shock cell structure in these flows directly correlates to understanding sound generation.
Coanda flows are present in rocketry where acoustic loading can actually damage vehicles and the atmosphere.
Modeling the shock cells and, thus, the sound generation will allow systems to be optimized to reduce acoustic loading.
To model shock cells the jet boundary must first be characterized.
Previous work has used hand selected points of the boundary, creating significant errors in jet boundary models.

This code seeks to see if the jet boundary can be extracted using Canney edge detection.
The project also seeks to understand how the jet boundary responds to slot width and pressure changes by
creating lines of best fit to quantify the changes in the boundary.

# What you need:
This project requires Numpy, OpenCV, and Matplotlib.
Scipy is optional to play with some edge detection algorithms I created.
I recommend using ImageJ to tare images. The images can be tared in OpenCV but ImageJ makes it really easy to run
basic preprocessing and create an apply masks if needed.

# File List and Guide
The primary files are listed below
1. Canney Find Edge Calibration: This file allows the user to figure out what Canney Thresholds and filter parameters
    are best for a data set using a simple GUI
2. Q1 is the data viable: This file demonstrates that the boundary edge can be found.
3. Q2 impact of pressureV2: This file detects and plots the changes in the jet boundary due to changes in pressure
4. Q3 impact of slotwidth: This file detects and plots the changes in the jet boundary due to changes in Slot Width

Optional files:
1. FindEdgeScan: attempt to write an algorithm to find the boundary
2. FindEdgeScan2: attempt to write an algorithm to find the boundary
3. FindEdgeScan3: attempt to write an algorithm to find the boundary
4. FindEdgeScanD: attempt to write an algorithm to find the boundary
5. Q2 impact of pressure: Older version
# How to use
Pre-processing:
To use this code a set of tared images need to be made. This can be done in open CV by subtracting two grayscale images
from each other. I will demonstrate how I preprocessed the images using ImageJ because I needed to generate a mask for
some images as well. Future iterations of this code would be able to perform these operations automatically or imageJ
would be used to preprocess the entire dataset in a few steps.

To tare an image you take a background image and subtract it from an image with a jet to highlight the jet.
This data set did not include any true background images so I found images that had the same slotwidth and used an
image with a pressure so low that the jet couldn't be seen.
Without this pre-processing step the edge selection doesn't really work.

![img_5.png](img_5.png)
load the files into ImageJ and find the image calculator


![img_6.png](img_6.png)
subtract images


![img_7.png](img_7.png)
Save the result to a Jpeg

After image taring it may be necessary to mask out unwanted artifacts

![img_10.png](img_10.png)
One can free select an area on an image as seen in the image above and select create mask

![img_11.png](img_11.png)
Finally, subtract the mask to remove any unwanted artifacts in the selected region.

Use of files


Canny find edge Calibration:
This file allows one to select filter parameters and canney edge detection thresholds that work for a data set.
To use this file add a file path into the path array in line 25 and select the index of the path in line 36.
The apply canny method can be edited on line 17 to adjust the filter settings. The only parameter that seems to
impact the results is the d value in the bilateral filter.
Once the file is running, the slider bars can be used to adjust the edges until the edges of the jet are clear and other 
features are not right of the boundary.

not great.
![img_13.png](img_13.png)

Thresholds adjusted until the edges are clear.
![img_12.png](img_12.png)

The results of the file can be used in Q1,Q2 and Q3.

Q1:
Demonstrates how the process works to get points on the Jet boundary edge.
It can be used to verify that parameters chosen will work through the entire process and choose what set of points 
to select. The extract_edges() method in this file can be adjusted to only grab points in a range of rows that result
in a clean boundary, otherwise edges from
To use the file
![img_9.png](img_9.png)

Q2 & Q3
The operation of both of these files is essentially the same


# sample results

![img_8.png](img_8.png)



# program limitations


# future work

