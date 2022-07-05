import cv2
captura=cv2.VideoCapture('videoprueba.avi')#se coloca el numero de camara si desea gravar o el nombre del video
#salida=cv2.VideoWriter('videoprueba.avi',cv2.VideoWriter_fourcc( * 'XVID' ),5,(640,480)) #grabar video

while(captura.isOpened()):
    ret,imagen=captura.read()
    if ret==True:
        cv2.imshow('video',imagen)
        #salida.write(imagen)
        if cv2.waitKey(30) &  0xFF == ord('f'): # waitkey variar para reproduccion rapida o lenta
            break
    else : break # al reproducir un video al finalizar me cierre la ventana 

captura.release()
#salida.release()
cv2.destroyAllWindows
