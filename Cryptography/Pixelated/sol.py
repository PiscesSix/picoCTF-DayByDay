from pylab import imread
import matplotlib.pyplot as plt

image1 = imread("scrambled1.png")
image2 = imread("scrambled2.png")

img = (image1 + image2)*255 % 256
imgplot = plt.imshow(img)
plt.show()