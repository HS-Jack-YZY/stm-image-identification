import cv2
import numpy as np
import sys
import os

def match_template(big_image_path, small_image_path):
    # 加载大图和小图
    img = cv2.imread(big_image_path, 0)
    template = cv2.imread(small_image_path, 0)

    # 获取小图的宽度和高度
    w, h = template.shape[::-1]

    # 使用matchTemplate函数来找到小图在大图中的位置
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # 使用minMaxLoc函数来获取匹配结果的最大和最小值，以及它们的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 使用矩形函数在大图上标记出小图的位置
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    return top_left, bottom_right

def small_image_path_gen(image_type, sample_num, image_num):
    """
    生成小图像路径。

    参数：
    image_type (int) -- 图像类型，0表示正常图像，1表示STM图像
    sample_num (int) -- 样本编号
    image_num (int) -- 图像编号

    返回：
    small_image_path (str) -- 小图像路径
    """

    if image_type == 0:
        image_type_path = "normal"
    elif image_type == 1:
        image_type_path = "stm"
    else:
        print("image_type error!")
        sys.exit(1)

    small_image_path = os.path.join("samples", image_type_path,
                                     "sample" + str(sample_num).zfill(2), 
                                     "small_image", 
                                     "small_image_" + str(image_num).zfill(2) + 
                                     ".jpg")
    return small_image_path

def big_image_path_gen(image_type, sample_num):
    """
    生成大图像路径。

    参数：
    image_type (int) -- 图像类型，0表示正常图像，1表示STM图像。
    sample_num (int) -- 样本编号。

    返回：
    big_image_path (str) -- 大图像路径。
    """

    if image_type == 0:
        image_type_path = "normal"
    elif image_type == 1:
        image_type_path = "stm"
    else:
        print("image_type error!")
        sys.exit(1)

    big_image_path = os.path.join("samples", image_type_path,
                                     "sample" + str(sample_num).zfill(2), 
                                     "big_image", 
                                     "big_image" + 
                                     ".jpg")
    return big_image_path


# 用于测试的主函数
if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     print('Usage: python match_template.py big_image_path small_image_path')
    #     sys.exit(1)

    # 使用命令行时用argv[]来获取参数
    # big_image_path = sys.argv[1]
    # small_image_path = sys.argv[2]
        
    # 使用IDE时用下面的参数
    #----------------------------------------------------
    # 图片类型：0-普通，1-stm
    image_type = 0
    # 样本编号
    sample_num = 1
    # 图片编号
    image_num = 1
    #----------------------------------------------------

    # 生成小图路径
    small_image_path = small_image_path_gen(image_type, sample_num, image_num)
    # 生成大图路径
    big_image_path = big_image_path_gen(image_type, sample_num)
    # 获取小图在大图中的位置
    top_left, bottom_right = match_template(big_image_path, small_image_path)

    # 加载大图
    img = cv2.imread(big_image_path)

    # 标记小图在大图中的位置
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    # 显示结果
    cv2.imshow('Detected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
