# Pixelated
## AUTHOR: SARA

### Description:
I have these 2 images, can you make a flag out of them? [srambled1.png](https://mercury.picoctf.net/static/1594c3f1980e3fb93df09a6d02f53904/scrambled1.png) [srambled2.png](https://mercury.picoctf.net/static/1594c3f1980e3fb93df09a6d02f53904/scrambled2.png)

## 1. Knowledge
- The concept of Visual Cryptography; this video provides a lot of knowledge about it: [Matthew Donato](https://youtu.be/bb24mBADuG0?si=2nFcQjx6x78dRtNd)

- While contemplating, I realized that by combining two images, we can unveil the hidden information.

## 2. Solution:

```py
from pylab import imread
import matplotlib.pyplot as plt

image1 = imread("scrambled1.png")
image2 = imread("scrambled2.png")

img = (image1 + image2)*255 % 256
imgplot = plt.imshow(img)
plt.show()
```

<p align="center">
  <img src="https://media.giphy.com/media/3o6nV13AMj5tac9MlO/giphy.gif" />
</p>

---

minhchi
