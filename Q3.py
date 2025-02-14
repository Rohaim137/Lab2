from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img =Image.open('images.jfif')
data=np.array(img)
plt.imshow(data)
plt.axis('off')
plt.title('Original Image')
plt.show()
data2=np.rot90(data,1,(0,1))
plt.imshow(data2)
plt.axis('off')
plt.title('Rotated Image')
plt.show()
data3=np.fliplr(data)
plt.imshow(data3)
plt.axis('off')
plt.title('Flipped Image')
plt.show()
def grayscale(rgb):
        return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
gray_array = grayscale(data)
plt.imshow(gray_array, cmap=plt.get_cmap('gray'))  # Use a grayscale colormap
plt.axis('off')
plt.title('Grayscale Image')
plt.show()