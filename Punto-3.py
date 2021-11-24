import cv2

import numpy as np
Img = cv2.imread(r'C:\Users\sngh9\OneDrive\Escritorio\Maestria_Semestre_2\Procesamiento_de_imagenes\Parcial\soccer_game.png')
image_draw = Img.copy()
points = []
print(Img.shape)

#Funciones para calcular rectas
def punto_rexta(b,m,x):
    y = m*x+b
    return (x,y)


def slope(p1,p2):
    x1,y1=p1
    x2,y2=p2
    if x2!=x1:
        return((y2-y1)/(x2-x1))
    else:
        return 'NA'


def drawLine(image,p1,p2,color = (0, 0, 255)):
    x1,y1=p1
    x2,y2=p2

    m=slope(p1,p2)

    h,w=image.shape[:2]

    if m!='NA':

        px=0
        py=-(x1-0)*m+y1

        qx=w
        qy=-(x2-w)*m+y2
    else:

        px,py=x1,0
        qx,qy=x1,h
    cv2.line(image, (int(px), int(py)), (int(qx), int(qy)), color, 2)
    return image

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

points1 = []
points2 = []
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", click)

point_counter = 0
while True:
    cv2.imshow("Image", image_draw)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("x"):
        points1 = points.copy()
        points = []
        break
    if len(points) > point_counter:
        point_counter = len(points)
        cv2.circle(image_draw, (points[-1][0], points[-1][1]), 3, [0, 0, 255], -1)
        #print(type(points),len(points))
    point_counter = 0
print(points1[0])
print(points1[1])
cv2.line(image_draw, points1[0], points1[1], [0, 0, 255], 1)
#cv2.drawContours(image_draw, [np.array(points1)], 0, (255,255,255), 2)
image_draw = drawLine(image_draw, points1[0], points1[1])
#Calcular la pendiente para que con ella pintar recta paralela, dos rectas paralelas tienen la misma pendiente
pendiente = slope(points1[0], points1[1])

while True:
    cv2.imshow("Image", image_draw)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("x"):
        points2 = points.copy()
        points = []
        break
    if len(points) > point_counter:
        point_counter = len(points)
        cv2.circle(image_draw, (points[-1][0], points[-1][1]), 3, [255, 0, 0], -1)
print( np.array(points2))
# Calculo de punto de corte basadi en la ecuación de la recta y = mx+b
b = points2[0][1]-(points2[0][0]*pendiente)
#print(b)
Punto2 = punto_rexta(b,pendiente,500) # calculo de un punto cualquiera basado en en el punto 2 marcado
print(Punto2)
N = min(len(points1), len(points2))
image_draw = drawLine(image_draw, points2[0], Punto2,color=(255,0,0))
assert N >=1, 'Only 2'
cv2.imshow("Image", image_draw)
cv2.waitKey(0)
pts1 = np.array(points1)
pts2 = np.array(points2)
print(pts1,pts2)

# Fuente de las Funciones draw line y slope :https://stackoverflow.com/questions/18632276/how-to-draw-a-line-on-an-image-in-opencv tuve que recurrir a esto para estirar las lineas de cv.line