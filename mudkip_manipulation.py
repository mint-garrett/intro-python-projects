##attempting to manipulate the small_mudkip png with opencv, it wasn't  sure successful or lengthyw

import cv2
import numpy as np
import matplotlib.pyplot as mp
from PIL import Image
from IPython.display import Image
import sys

np.set_printoptions(threshold = sys.maxsize)

small_mudkip = cv2.imread("/home/garrett/Documents/code/code.py/openCV_py/small_mudkip.png",1)
small_mudkip_rbg = cv2.cvtColor(small_mudkip, cv2.COLOR_BGR2RGB)
mp.imshow(small_mudkip_rbg)
mp.show()

print(small_mudkip_rbg[0,0])
print(small_mudkip_rbg[287,269])

mudkip_copy = small_mudkip_rbg.copy()
mudkip_copy[287,269] = 255
mp.imshow(mudkip_copy)
mp.show()

resize_mudkip10x = cv2.resize(small_mudkip, None, fx=2, fy=2)
mp.imshow(resize_mudkip10x)
mp.show()

