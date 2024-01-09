
import cv2
import numpy as np
import sys
import os

# 大图小图所在位置
big_image_address = 'samples/big_image'
small_image_address = 'samples/small_image'

# 加载大图和小图
img = cv2.imread(os.path.join(big_image_address, 'big_image.jpg'), 0)
template = cv2.imread(os.path.join(small_image_address, 'noisy_image.jpg'), 0)

# 获取小图的宽度和高度
w, h = template.shape[::-1]

# 使用matchTemplate函数来找到小图在大图中的位置
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# 使用minMaxLoc函数来获取匹配结果的最大和最小值，以及它们的位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 使用矩形函数在大图上标记出小图的位置
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, 255, 2)

# 显示结果
cv2.imshow('Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()