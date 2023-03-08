import numpy as np
import cv2


# if __name__ == "__main__":
#
#     accuracy_num = 0
#
#     # for i in range(50):
#
#         # img : original image
#         # path = '/home/archer/CODE/Number_Segmentation/dataset2/' + str(i+1) + '.png'
#     path = "4.jpg"
#     img = cv2.imread(path)
#
#     # img1 : resize image
#     img1 = cv2.resize(img, (320, 100), interpolation=cv2.INTER_AREA)
#
#     # img2 : gray image
#     img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#
#     # img3 : noise reduction image
#     img3 = cv2.bilateralFilter(img2, 11, 17, 17)
#
#     # img4 : texture information image
#     img4 = cv2.Canny(img3, 50, 150)
#
#     # img5 : image removal image
#     img5 = img4[10:90, 10:310]
#     crop_img = img1[10:90, 10:310, :]
#
#     img, contours, hierarchy = cv2.findContours(img5, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     candidate = []
#     for cnt in contours:
#         x, y, w, h = cv2.boundingRect(cnt)
#
#         if w*h < 500:
#             continue
#         if w * h > 4000:
#             continue
#         if h < 20:
#             continue
#         if w > 80:
#             continue
#
#         candidate.append([x, (x + w)])
#
#     loc = np.zeros(300)
#
#     for j in range(len(candidate)):
#         x1 = candidate[j][0]
#         x2 = candidate[j][1]
#         loc[x1:x2] = 1
#
#     start = []
#     end = []
#
#     if loc[0] == 1:
#         start.append(0)
#
#     for j in range(300-1):
#         if loc[j] == 0 and loc[j+1] == 1:
#             start.append(j)
#         if loc[j] == 1 and loc[j+1] == 0:
#             end.append(j)
#
#     if loc[299] == 1:
#         end.append(299)
#
#     print('Character start coordination : ', start, len(start))
#     print('Character end coordination : ', end, len(start))
#
#     if len(start) == 7 and len(end) == 7:
#
#         print('The Segmentation looks well ! ')
#
#         cv2.rectangle(crop_img, (0, 0), (start[1]-5, 80), (0, 0, 255), 2)
#
#         for j in range(1, 7):
#             x1 = start[j]
#             x2 = end[j]
#             y1 = 0
#             y2 = 80
#             cv2.rectangle(crop_img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#
#         accuracy_num = accuracy_num + 1
#
#     cv2.namedWindow("final_crop_img")
#     cv2.imshow("final_crop_img", crop_img)
#     cv2.waitKey(0)
#
#         # cv2.imwrite('/home/archer/CODE/Number_Segmentation/demo/' + str(i+1) + '.jpg', crop_img)
#
#     print('The character segmentation accuracy : ', accuracy_num/50)


def char_splitting(path):
    accuracy_num = 0
    img = cv2.imread(path)
    img1 = cv2.resize(img, (320, 100), interpolation=cv2.INTER_AREA)
    img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img3 = cv2.bilateralFilter(img2, 11, 17, 17)
    img4 = cv2.Canny(img3, 50, 150)
    img5 = img4[10:90, 10:310]
    crop_img = img1[10:90, 10:310, :]

    img, contours, hierarchy = cv2.findContours(img5, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    candidate = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        if w*h < 500:
            continue
        if w * h > 4000:
            continue
        if h < 20:
            continue
        if w > 80:
            continue

        candidate.append([x, (x + w)])

    loc = np.zeros(300)

    for j in range(len(candidate)):
        x1 = candidate[j][0]
        x2 = candidate[j][1]
        loc[x1:x2] = 1

    start = []
    end = []

    if loc[0] == 1:
        start.append(0)

    for j in range(300-1):
        if loc[j] == 0 and loc[j+1] == 1:
            start.append(j)
        if loc[j] == 1 and loc[j+1] == 0:
            end.append(j)

    if loc[299] == 1:
        end.append(299)
    # print('Character start coordination : ', start, len(start))
    # print('Character end coordination : ', end, len(start))

    for i in range(7):
        cropped_img = crop_img[0:80, start[i]:end[i]]
        cv2.imwrite('segmentation/' + str(i) + '.jpg', cropped_img)

    if len(start) == 7 and len(end) == 7:

        print('The Segmentation looks well ! ')

        cv2.rectangle(crop_img, (0, 0), (start[1]-5, 80), (0, 0, 255), 2)

        for j in range(1, 7):
            x1 = start[j]
            x2 = end[j]
            y1 = 0
            y2 = 80
            cv2.rectangle(crop_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        accuracy_num = accuracy_num + 1

    cv2.namedWindow("final_crop_img")
    cv2.imshow("final_crop_img", crop_img)
    cv2.waitKey(0)

    # for i in range(7):
    #     cropped_image = crop_img[start[]]

    # cv2.imwrite(r'D:\personal_srcs\IcDesignandDebug' + str(i+1) + '.jpg', crop_img)

    print('The character segmentation accuracy : ', accuracy_num/50)

char_splitting(r'D:\personal_srcs\IcDesignandDebug\plates\img0.jpg')




