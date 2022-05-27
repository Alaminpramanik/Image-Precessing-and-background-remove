from skimage import io as skio
from skimage import filters
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

url = 'http://i.stack.imgur.com/SYxmp.jpg'
img = skio.imread(url)

sobel = filters.sobel(img)

plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['figure.dpi'] = 200
plt.imshow(sobel)

blurred = filters.gaussian(sobel, sigma=2.0)
plt.imshow(blurred)

light_spots = np.array((img > 245).nonzero()).T
light_spots.shape

plt.plot(light_spots[:, 1], light_spots[:, 0], 'o')
plt.imshow(img)
plt.title('light spots in image')
dark_spots = np.array((img < 3).nonzero()).T
dark_spots.shape

plt.plot(dark_spots[:, 1], dark_spots[:, 0], 'o')
plt.imshow(img)
plt.title('dark spots in image')
# print("shape of image: {}".format(img.shape))
# print("dtype of image: {}".format(img.dtype))

# print("dtype of sobel: {}".format(sobel.dtype))