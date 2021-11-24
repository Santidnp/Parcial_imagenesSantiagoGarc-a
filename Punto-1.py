import cv2
import matplotlib.pyplot as plt
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
cv2.imshow("Image", mask)
cv2.waitKey(0)
Total_de_pixeles = mask.shape[0]*mask.shape[1]

(unique, counts) = np.unique(mask, return_counts=True)
frequencies = np.asarray((unique, counts)).T

Pixeles_cesped  = frequencies[1,1]
print('Porcentaje de cesped: ',Pixeles_cesped/Total_de_pixeles)
