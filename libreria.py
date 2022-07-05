import cv2
import numpy as np

def rojo():

    captura=cv2.VideoCapture('video11.mp4')
     #salida=cv2.VideoWriter('videoprueba.avi',cv2.VideoWriter_fourcc( * 'XVID' ),5,(640,480)) #grabar video
    #rango del color 
    #primer rango
    rojobajo = (0, 100, 20) 
    rojoAlto = (8, 255, 255)

    #segundo rango
    rojoBajo1= (175, 100, 20)
    rojoAlto1= (179, 255, 255)

    while True:
        ret,imagen=captura.read()
        if ret==True:
            imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
            maskRojo1 = cv2.inRange(imagenHSV, rojobajo, rojoAlto) #buscar el rango del color
            maskRojo2 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
            maskRojo = cv2.add(maskRojo1, maskRojo2) #como son dos rangos, une los dos en uno solo
            maskRojo3 = cv2.bitwise_and(imagen, imagen, mask= maskRojo)
            cv2.imshow('imagen',imagen)
            cv2.imshow('maskRojo', maskRojo) #visualizacion muestra el color en blanco y el resto en negro
            cv2.imshow('maskRojo3', maskRojo3) #muestra el color y el resto en negro
            #salida.write(imagen)
        if cv2.waitKey(1) &  0xFF == ord('r'): # waitkey variar para reproduccion rapida o lenta
            break
    

    captura.release()
    #salida.release()
    cv2.destroyAllWindows

    menu()

#----------------------------------------------------------------

def azul():

    captura=cv2.VideoCapture('video11.mp4')

    azulbajo = (100, 100, 20) 
    azulAlto = (130, 255, 255)

    while True:
        ret,imagen=captura.read()
        if ret==True:
            imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
            maskazul = cv2.inRange(imagenHSV, azulbajo, azulAlto) #buscar el rango del color
            maskazul2 = cv2.bitwise_and(imagen, imagen, mask= maskazul)
            #contornos= cv2.findContours(maskazul,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            
            
            #for c in contornos:

                #area = cv2.contourArea(c)

                #if area > 3000:
                    #cv2.drawContours(imagen, [c], 0, (255,0,0), 3)



            #maskazul2 = cv2.bitwise_and(imagen, imagen, mask= maskazul)
            cv2.imshow('imagen',imagen)
            #cv2.imshow('maskazul', maskazul) #visualizacion muestra el color en blanco y el resto en negro
            cv2.imshow('maskazul2', maskazul2) #muestra el color y el resto en negro
            
        if cv2.waitKey(1) &  0xFF == ord('a'): # waitkey variar para reproduccion rapida o lenta
            break
    

    captura.release()
    cv2.destroyAllWindows
    menu()

#------------------------------------------------------------------------------------------------------------------------

def amarillo():

    captura=cv2.VideoCapture('video11.mp4')

    amaribajo = (15, 100, 20) 
    amariAlto = (40, 255, 255)

    while True:
        ret,imagen=captura.read()
        if ret==True:
            imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
            maskamari = cv2.inRange(imagenHSV, amaribajo, amariAlto) #buscar el rango del color
            maskamari2 = cv2.bitwise_and(imagen, imagen, mask= maskamari)
           
            cv2.imshow('imagen',imagen)
            #cv2.imshow('maskamari', maskamari) #visualizacion muestra el color en blanco y el resto en negro
            cv2.imshow('maskamari2', maskamari2) #muestra el color y el resto en negro
            
        if cv2.waitKey(1) &  0xFF == ord('m'): # waitkey variar para reproduccion rapida o lenta
            break
    

    captura.release()
    cv2.destroyAllWindows
    menu()

#----------------------------------------------------------------------------------------------------


def todos():
    captura=cv2.VideoCapture('video11.mp4')

    rojobajo = (0, 100, 20) 
    rojoAlto = (8, 255, 255)
    rojoBajo1=(175, 100, 20)
    rojoAlto1=(179, 255, 255)

    azulbajo = (100, 100, 20) 
    azulAlto = (130, 255, 255)

    amaribajo = (15, 100, 20) 
    amariAlto = (40, 255, 255)

    while True:
        ret,imagen=captura.read()
        if ret==True:
            imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
            
            maskRojo1 = cv2.inRange(imagenHSV, rojobajo, rojoAlto) #buscar el rango del color
            maskRojo2 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
            maskRojo = cv2.add(maskRojo1, maskRojo2) #como son dos rangos, une los dos en uno solo
            
            maskazul = cv2.inRange(imagenHSV, azulbajo, azulAlto) #buscar el rango del color
            maskamari = cv2.inRange(imagenHSV, amaribajo, amariAlto) #buscar el rango del color
            maskazulamari = cv2.add(maskazul, maskamari)
           

            masktodos = cv2.add(maskRojo, maskazulamari) 
            masktodos1 = cv2.bitwise_and(imagen, imagen, mask= masktodos)
           
            cv2.imshow('imagen',imagen)
            cv2.imshow('masktodos', masktodos) #visualizacion muestra el color en blanco y el resto en negro
            cv2.imshow('masktodos1', masktodos1) #muestra el color y el resto en negro
            
        if cv2.waitKey(1) &  0xFF == ord('t'): # waitkey variar para reproduccion rapida o lenta
            break
    

    captura.release()
    cv2.destroyAllWindows
    menu()

    

    

    
    












#--------------------------------------------------------------------------------------------------------------------------
def menu (): #menu principal
    print ('''DETECTOR DE COLORES PRIMARIOS
DIJITE EL NUMERO SEGUN EL COLOR QUE DESEA DETECTAR 
1.COLOR ROJO
2.COLOR AZUL
3.COLOR AMARILLO
4.TODOS LOS COLORES AL TIEMPO
5.SALIR
''')
    op=int(input('ingrese su eleccion:\n'))
    
    if op==1:
        rojo()
        
    elif op==2:
        azul()
        
    elif op==3:
       
        amarillo()
        
    elif op==4:
        todos()

    elif op==5:
        exit()
    else:
        print('error de ingreso, seleccione un numero correcto')
        menu()
menu()


