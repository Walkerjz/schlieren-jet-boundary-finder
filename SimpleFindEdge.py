import matplotlib.pyplot as plt
import numpy as np
#choose file
filepath = 'Data/rcphoto2370um30psi_2019.jpg'
#load image
img = plt.imread(filepath)
#convert to array
img_array = np.array(img)
subimg = img[280:514, 326:594]
threshold = np.mean(subimg)
column = 400
threshold = 10/306*(column-300)+60
plt.plot(img_array[:,column])
plt.plot(threshold*np.ones(369))
plt.show()