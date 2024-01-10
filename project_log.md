## 2023.01.09

编写了python文件`testOpenCV.py`，实现大图中找小图的操作。

`testOpenCV.py`代码如下：

```python
import cv2
import numpy as np
import sys
import os

# 大图小图所在位置
big_image_address = 'samples/big_image'
small_image_address = 'samples/small_image'

# 加载大图和小图
img = cv2.imread(os.path.join(big_image_address, 'big_image.jpg'), 0)
template = cv2.imread(os.path.join(small_image_address, 'small_image.jpg'), 0)

# 获取小图的宽度和高度
w, h = template.shape[::-1]

# 使用matchTemplate函数来找到小图在大图中的位置
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# 使用minMaxLoc函数来获取匹配结果的最大和最小值，以及它们的位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 使用矩形函数在大图上标记出小图的位置
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, 
              top_left, bottom_right, 255, 2)

# 显示结果
cv2.imshow('Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### TODO

* 每次改变样本，都需要重新修改代码。
* 得到的图片没有保存。
* 可以讲专门用途的代码重构为函数。

## 2023.01.10

### 15:10

修改了testOpenCV.py文件，实现了如下功能：

1. 每次变更图片只需要修改三个参数（）