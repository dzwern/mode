import cv2
import numpy as np
import pytesseract as pt
import matplotlib.pyplot as plt

img_path = r'.\20220427115259.png'
#******************* 读取图片为灰度格式并查看 ********************#
img = cv2.imread(img_path,0)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.show()
# print(img)
#*************** 读取图片中的文字并输出（打印出来）***************#
text = pt.image_to_string(img, lang="chi_sim")
print(type(text),len(text))
print(text)
