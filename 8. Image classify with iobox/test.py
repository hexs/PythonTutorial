import numpy as np

img = np.full((3, 3, 3), (1, 2, 3), np.uint8)

print(img)
img = np.expand_dims(img, axis=0)
print(img)