# increasing the brightness of an image
import cv2
import numpy as np
from matplotlib import pyplot as plt

# load the image
img = cv2.imread('images/nature.jpeg')

# increase the brightness of the image by adding 50 to all pixel values
brigtness_matrix = np.ones(img.shape, dtype='uint8') * 50

# Use cv2.add to avoid negative values or overflow
brighter_img = cv2.add(img, brigtness_matrix)

brighter_rgb = cv2.cvtColor(brighter_img, cv2.COLOR_BGR2RGB)

plt.imshow(brighter_rgb)
plt.title('Brigther Image')
plt.show()

# save the image
cv2.imwrite('images/nature_brighter.jpeg', brighter_rgb)
print('Brighter image saved successfully')