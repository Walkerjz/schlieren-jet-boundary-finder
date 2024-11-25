import matplotlib.pyplot as plt
import numpy as np
#choose file
filepath = 'Data/rcphoto1810um5psi_2019.jpg'
#load image
img = plt.imread(filepath)
#convert to array
img_array = np.array(img)
plt.plot(img_array[:,150])
plt.show()
pass