import os


# file = r'D:\personal_srcs\IcDesignandDebug\lpr_data\0'
#
# for root, dirs, files in os.walk(file):
#     for file in files:
#         path = os.path.join(root, file)
#         print(path)

# a = ['苏', 'A', '1', '2']
# print(a)
# print("".join(a))

import cv2

# img = cv2.imread('4.jpg')
# print(img.shape)

# 1. 进行resize、灰度化、双边滤波降噪
# 2. canny边缘检测
# 3. findContours查找轮廓

# 车牌识别
import cv2
import numpy as np
import os


# # 提取车牌（形态学）
# # def Morph_Distinguish(img):
# #     # 1、转灰度图
# img = cv2.imread("6.png")
# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('gray', gray)
# cv2.waitKey(0)
# # 2、顶帽运算
# # gray = cv.equalizeHist(gray)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 17))
# tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
# cv2.imshow('tophat', tophat)
# cv2.waitKey(0)
#
# # 3、Sobel算子提取y方向边缘（揉成一坨）
# y = cv2.Sobel(tophat, cv2.CV_16S, 1, 0)
# absY = cv2.convertScaleAbs(y)
# cv2.imshow('absY', absY)
# cv2.waitKey(0)
# #
# # 4、自适应二值化（阈值自己可调）
# ret, binary = cv2.threshold(absY, 75, 255, cv2.THRESH_BINARY)
# cv2.imshow('binary', binary)
# cv2.waitKey(0)
# #
# # 5、开运算分割（纵向去噪，分隔）
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 15))
# Open = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
# cv2.imshow('Open', Open)
# cv2.waitKey(0)
# #
# # 6、闭运算合并，把图像闭合、揉团，使图像区域化，便于找到车牌区域，进而得到轮廓
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (41, 15))
# close = cv2.morphologyEx(Open, cv2.MORPH_CLOSE, kernel)
# cv2.imshow('close', close)
# cv2.waitKey(0)
# # #
# # 7、膨胀/腐蚀（去噪得到车牌区域）
# # 中远距离车牌识别
# kernel_x = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 7))
# kernel_y = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 11))
# # # 近距离车牌识别
# # kernel_x = cv2.getStructuringElement(cv2.MORPH_RECT, (79, 15))
# # kernel_y = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 31))
# # 7-1、腐蚀、膨胀（去噪）
# erode_y = cv2.morphologyEx(close, cv2.MORPH_ERODE, kernel_y)
# cv2.imshow('erode_y', erode_y)
# dilate_y = cv2.morphologyEx(erode_y, cv2.MORPH_DILATE, kernel_y)
# cv2.imshow('dilate_y', dilate_y)
# cv2.waitKey(0)
# # 7-1、膨胀、腐蚀（连接）（二次缝合）
# dilate_x = cv2.morphologyEx(dilate_y, cv2.MORPH_DILATE, kernel_x)
# cv2.imshow('dilate_x', dilate_x)
# erode_x = cv2.morphologyEx(dilate_x, cv2.MORPH_ERODE, kernel_x)
# cv2.imshow('erode_x', erode_x)
# cv2.waitKey(0)
# # #
# # 8、腐蚀、膨胀：去噪
# kernel_e = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 9))
# erode = cv2.morphologyEx(erode_x, cv2.MORPH_ERODE, kernel_e)
# cv2.imshow('erode', erode)
# cv2.waitKey(0)
# kernel_d = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 11))
# dilate = cv2.morphologyEx(erode, cv2.MORPH_DILATE, kernel_d)
# cv2.imshow('dilate', dilate)
# cv2.waitKey(0)
#
# # 9、获取外轮廓
# img_copy = img.copy()
# # 9-1、得到轮廓
# img0, contours, hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# # 9-2、画出轮廓并显示
# cv2.drawContours(img_copy, contours, -1, (255, 0, 255), 2)
# cv2.imshow('Contours', img_copy)
# cv2.waitKey(0)
# #
# # 10、遍历所有轮廓，找到车牌轮廓
# i = 0
# for contour in contours:
#     # 10-1、得到矩形区域：左顶点坐标、宽和高
#     rect = cv2.boundingRect(contour)
#     # 10-2、判断宽高比例是否符合车牌标准，截取符合图片
#     if rect[2] > rect[3] * 3 and rect[2] < rect[3] * 5:
#         # 截取车牌并显示
#         print(rect)
#         img = img[(rect[1] - 5):(rect[1] + rect[3] + 5), (rect[0] - 5):(rect[0] + rect[2] + 5)]  # 高，宽
#         # cv2.imshow('plate', img)
#         try:
#             cv2.imshow('license plate', img)
#             cv2.imwrite('plates/img%d.jpg' % (i), img)
#             i += 1
#         except:
#             pass
#
# cv2.waitKey(0)
# #
# #
# # if __name__ == '__main__':
# #     global count
# #     count = 0
# #     # 遍历文件夹中的每张图片（车）
# #     for car in os.listdir('cars'):
# #         # 1、获取路径
# #         path = 'cars/' + 'car' + str(count) + '.jpg'
# #         # 2、获取图片
# #         img = cv.imread(path)
# #         # 3、定位车牌
# #         Morph_Distinguish(img)  # 形态学提取车牌
# #         count += 1
# #
# #     cv.waitKey(0)
#
# def licensePlateExtraction(path):
#     img = cv2.imread(path)
#     gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 17))
#     tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
#
#     y = cv2.Sobel(tophat, cv2.CV_16S, 1, 0)
#     absY = cv2.convertScaleAbs(y)
#
#     ret, binary = cv2.threshold(absY, 75, 255, cv2.THRESH_BINARY)
#
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 15))
#     Open = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
#
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (41, 15))
#     close = cv2.morphologyEx(Open, cv2.MORPH_CLOSE, kernel)
#
#     kernel_x = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 7))
#     kernel_y = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 11))
#
#     erode_y = cv2.morphologyEx(close, cv2.MORPH_ERODE, kernel_y)
#     dilate_y = cv2.morphologyEx(erode_y, cv2.MORPH_DILATE, kernel_y)
#
#     dilate_x = cv2.morphologyEx(dilate_y, cv2.MORPH_DILATE, kernel_x)
#
#     erode_x = cv2.morphologyEx(dilate_x, cv2.MORPH_ERODE, kernel_x)
#
#     kernel_e = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 9))
#     erode = cv2.morphologyEx(erode_x, cv2.MORPH_ERODE, kernel_e)
#
#     kernel_d = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 11))
#     dilate = cv2.morphologyEx(erode, cv2.MORPH_DILATE, kernel_d)
#
#     img_copy = img.copy()
#
#     img0, contours, hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     cv2.drawContours(img_copy, contours, -1, (255, 0, 255), 2)
#     cv2.imshow('Contours', img_copy)
#     cv2.waitKey(0)
#
#     i = 0
#     for contour in contours:
#         rect = cv2.boundingRect(contour)
#         if rect[2] > rect[3] * 3 and rect[2] < rect[3] * 5:
#             print(rect)
#             img = img[(rect[1] - 5):(rect[1] + rect[3] + 5), (rect[0] - 5):(rect[0] + rect[2] + 5)]
#             try:
#                 cv2.imshow('license plate', img)
#                 cv2.imwrite('plates/img%d.jpg' % (i), img)
#                 i += 1
#             except:
#                 pass
#
#     cv2.waitKey(0)

# directory = r'D:\personal_srcs\IcDesignandDebug\segmentation'
#
# for root, dirs, files in os.walk(directory):
#     for file in files:
#         path = os.path.join(root, file)
#         print(path)

classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '川', '鄂', '赣', '甘', '贵', '桂', '黑', '沪', '冀', '津', '京', '吉', '辽', '鲁', '蒙',
           '闽', '宁', '青', '琼', '陕', '苏', '晋', '皖', '湘', '新', '豫', '渝', '粤', '云', '藏', '浙']

print(classes[0])