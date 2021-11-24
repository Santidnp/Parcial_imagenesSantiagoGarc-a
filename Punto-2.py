import cv2

import numpy as np
Img = cv2.imread(r'C:\Users\sngh9\OneDrive\Escritorio\Maestria_Semestre_2\Procesamiento_de_imagenes\Parcial\soccer_game.png')
image_hsv = cv2.cvtColor(Img, cv2.COLOR_BGR2HSV)

hist_hue = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])

max_val = hist_hue.max()
max_pos = int(hist_hue.argmax())
lim_inf = (max_pos - 10, 0, 0)
lim_sup = (max_pos + 10, 255, 255)
mask = cv2.inRange(image_hsv, lim_inf, lim_sup)
mask_not = cv2.bitwise_not(mask)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 1280, 720)
res = cv2.bitwise_and(Img,Img,mask = mask_not)
#cv2.imshow("Image", res)
#cv2.waitKey(0)
res= cv2.convertScaleAbs(res)
contours, hierarchy = cv2.findContours(mask_not, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image_draw = Img.copy()
contador_jugardores = 0
for idx, cont in enumerate(contours):
    if len(contours[idx]) > 20:
        #hull = cv2.convexHull(contours[idx])
        #cv2.drawContours(image_draw, contours, idx, (0, 255, 255), 2)
        #cv2.drawContours(image_draw, [hull], 0, (255, 0, 0), 2)
        #M = cv2.moments(contours[idx])
        #cx = int(M['m10'] / M['m00'])
        #cy = int(M['m01'] / M['m00'])
        #area = M['m00']
        x, y, width, height = cv2.boundingRect(contours[idx])
        area = width * height
        if area > 900 and area < 100000:
            cv2.rectangle(image_draw, (x, y), (x + width, y + height), (0, 0, 255), 2)
            contador_jugardores +=1
        #print(x,y,x + width, y + height )
        #print(width*height)
        #(x, y), radius = cv2.minEnclosingCircle(contours[idx])
        #center = (int(x), int(y))
        #radius = int(radius)
        #cv2.circle(image_draw, center, radius, (0, 255, 0), 2)
cv2.resizeWindow("Image", 1280, 720)
cv2.imshow("Image", image_draw)
cv2.waitKey(0)
print('Número de Jugadores y arbitros encontrados = ', contador_jugardores)
