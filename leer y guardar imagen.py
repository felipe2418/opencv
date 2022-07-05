import cv2

imagen=cv2.imread('ojo.jpg',0) #0 para escala en gris y 1 original o a color
cv2.imshow('prueba',imagen) 
cv2.imwrite('ojogris.jpg',imagen)
cv2.waitKey(5000)
cv2.destroyAllWindows()
