import os
import pandas as pd
import cv2

image = cv2.imread('./Spine Dataset/data/training/sunhl-1th-02-Jan-2017-162 A AP.jpg')
h, w, c = image.shape

df = pd.read_csv('./Example.csv')

x_list = []
y_list = []

for index, value in enumerate(df):
    if len(value.split('.')) > 2:
        value = value[:-2]

    if index < 68:
        x_list.append(float(value))
    else:
        y_list.append(float(value))

point_list = []

for i in range(0, len(x_list)):
    point_list.append([int(x_list[i] * w), int(y_list[i] * h)])

for point in point_list:
    cv2.circle(image, point, 5, (0, 0, 255), -1)

cv2.imwrite('./Example.png', image)